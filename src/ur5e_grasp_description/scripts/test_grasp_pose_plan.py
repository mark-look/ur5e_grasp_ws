#!/usr/bin/env python3

import sys
import rclpy

from rclpy.node import Node
from rclpy.action import ActionClient

from moveit_msgs.action import MoveGroup
from moveit_msgs.msg import (
    MotionPlanRequest,
    Constraints,
    PositionConstraint,
    OrientationConstraint,
    BoundingVolume,
    WorkspaceParameters
)

from shape_msgs.msg import SolidPrimitive
from geometry_msgs.msg import Pose


class GraspPosePlanner(Node):

    def __init__(self):
        super().__init__('grasp_pose_planner')

        self.client = ActionClient(
            self,
            MoveGroup,
            '/move_action'
        )

    def plan(self):

        self.get_logger().info('Waiting for MoveIt...')

        if not self.client.wait_for_server(timeout_sec=10.0):
            self.get_logger().error(
                'MoveIt action server unavailable!'
            )
            return

        goal = MoveGroup.Goal()

        request = MotionPlanRequest()

        # 规划组
        request.group_name = 'ur_manipulator'

        # OMPL
        request.pipeline_id = 'ompl'
        request.planner_id = ''

        request.num_planning_attempts = 5
        request.allowed_planning_time = 15.0

        request.max_velocity_scaling_factor = 0.05
        request.max_acceleration_scaling_factor = 0.05

        # 使用当前机器人状态
        request.start_state.is_diff = True

        # 工作空间
        workspace = WorkspaceParameters()
        workspace.header.frame_id = 'world'

        workspace.min_corner.x = -1.0
        workspace.min_corner.y = -1.0
        workspace.min_corner.z = 0.0

        workspace.max_corner.x = 1.5
        workspace.max_corner.y = 1.0
        workspace.max_corner.z = 1.8

        request.workspace_parameters = workspace

        # 目标位置
        target_x = 0.5065
        target_y = 0.0000
        target_z = 0.6900

        # 位置约束
        position_constraint = PositionConstraint()

        position_constraint.header.frame_id = 'world'
        position_constraint.link_name = 'tool0'
        position_constraint.weight = 1.0

        region = BoundingVolume()

        sphere = SolidPrimitive()
        sphere.type = SolidPrimitive.SPHERE
        sphere.dimensions = [0.01]

        sphere_pose = Pose()
        sphere_pose.position.x = target_x
        sphere_pose.position.y = target_y
        sphere_pose.position.z = target_z
        sphere_pose.orientation.w = 1.0

        region.primitives.append(sphere)
        region.primitive_poses.append(sphere_pose)

        position_constraint.constraint_region = region

        # 姿态约束
        orientation_constraint = OrientationConstraint()

        orientation_constraint.header.frame_id = 'world'
        orientation_constraint.link_name = 'tool0'

        orientation_constraint.orientation.x = -0.707
        orientation_constraint.orientation.y = 0.023
        orientation_constraint.orientation.z = 0.020
        orientation_constraint.orientation.w = 0.707

        orientation_constraint.absolute_x_axis_tolerance = 0.05
        orientation_constraint.absolute_y_axis_tolerance = 0.05
        orientation_constraint.absolute_z_axis_tolerance = 0.05

        orientation_constraint.weight = 1.0

        # 组合约束：本次只测试位置，不限制姿态
        constraints = Constraints()

        constraints.position_constraints.append(
            position_constraint
        )

        # 关键：只规划，不执行
        goal.planning_options.plan_only = True
        goal.planning_options.replan = False

        self.get_logger().info('================================')
        self.get_logger().info('Pre-grasp planning target:')
        self.get_logger().info(
            f'Position: [{target_x}, {target_y}, {target_z}]'
        )
        self.get_logger().info(
            'Orientation: [-0.707, 0.023, 0.020, 0.707]'
        )
        self.get_logger().info('Plan only: TRUE')
        self.get_logger().info('================================')

        send_future = self.client.send_goal_async(goal)

        rclpy.spin_until_future_complete(self, send_future)

        goal_handle = send_future.result()

        if goal_handle is None or not goal_handle.accepted:
            self.get_logger().error('Planning goal rejected!')
            return

        self.get_logger().info('Planning request accepted.')

        result_future = goal_handle.get_result_async()

        rclpy.spin_until_future_complete(self, result_future)

        result = result_future.result().result

        error_code = result.error_code.val

        self.get_logger().info(
            f'MoveIt error code: {error_code}'
        )

        points = result.planned_trajectory.joint_trajectory.points

        self.get_logger().info(
            f'Trajectory points: {len(points)}'
        )

        if error_code == 1 and len(points) > 0:

            self.get_logger().info(
                'PRE-GRASP PLANNING SUCCESS!'
            )

            for i, point in enumerate(points):
                self.get_logger().info(
                    f'Point {i}: {list(point.positions)}'
                )

        else:

            self.get_logger().error(
                'PRE-GRASP PLANNING FAILED!'
            )


def main(args=None):

    rclpy.init(args=args)

    node = GraspPosePlanner()

    try:
        node.plan()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()