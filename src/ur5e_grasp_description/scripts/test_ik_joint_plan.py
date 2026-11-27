#!/usr/bin/env python3

import math
import sys

import rclpy

from rclpy.node import Node
from rclpy.action import ActionClient

from moveit_msgs.action import MoveGroup
from moveit_msgs.msg import Constraints, JointConstraint


class IKJointPlanTest(Node):

    def __init__(self):
        super().__init__('ik_joint_plan_test')

        self.client = ActionClient(
            self,
            MoveGroup,
            '/move_action'
        )

    def run(self):

        self.get_logger().info('Waiting for MoveIt...')

        if not self.client.wait_for_server(timeout_sec=30.0):
            self.get_logger().error('MoveIt action server unavailable!')
            return 1

        goal = MoveGroup.Goal()
        request = goal.request

        request.group_name = 'ur_manipulator'
        request.pipeline_id = 'ompl'
        request.planner_id = ''

        request.num_planning_attempts = 5
        request.allowed_planning_time = 15.0

        request.max_velocity_scaling_factor = 0.05
        request.max_acceleration_scaling_factor = 0.05

        request.start_state.is_diff = True

        # IK 返回的六个关节角。
        # 对角度进行 2*pi 等效归一化，避免不必要的整圈旋转。
        ik_solution = {
            'shoulder_pan_joint': -3.052235987,
            'shoulder_lift_joint': -1.870451642,
            'elbow_joint': -0.845787743,
            'wrist_1_joint': 3.055680543,
            'wrist_2_joint': 2.947740223,
            'wrist_3_joint': -2.807810081,
        }

        target_positions = {
            name: math.atan2(math.sin(value), math.cos(value))
            for name, value in ik_solution.items()
        }

        constraints = Constraints()
        constraints.name = 'ik_joint_space_goal'

        for joint_name, position in target_positions.items():

            jc = JointConstraint()

            jc.joint_name = joint_name
            jc.position = position
            jc.tolerance_above = 0.003
            jc.tolerance_below = 0.003
            jc.weight = 1.0

            constraints.joint_constraints.append(jc)

        request.goal_constraints = [constraints]

        # 只规划，不执行
        goal.planning_options.plan_only = True
        goal.planning_options.replan = False

        self.get_logger().info('================================')
        self.get_logger().info('IK JOINT-SPACE PLANNING TEST')

        for name, value in target_positions.items():
            self.get_logger().info(
                f'{name}: {value:.6f} rad'
            )

        self.get_logger().info('Plan only: TRUE')
        self.get_logger().info('================================')

        send_future = self.client.send_goal_async(goal)

        rclpy.spin_until_future_complete(
            self,
            send_future,
            timeout_sec=35.0
        )

        if not send_future.done():
            self.get_logger().error('Planning request timeout!')
            return 1

        goal_handle = send_future.result()

        if goal_handle is None or not goal_handle.accepted:
            self.get_logger().error('Planning goal rejected!')
            return 1

        self.get_logger().info('Planning request accepted.')

        result_future = goal_handle.get_result_async()

        rclpy.spin_until_future_complete(
            self,
            result_future,
            timeout_sec=60.0
        )

        if not result_future.done():
            self.get_logger().error('Result timeout!')
            return 1

        wrapped_result = result_future.result()

        if wrapped_result is None:
            self.get_logger().error('No result returned!')
            return 1

        result = wrapped_result.result

        error_code = result.error_code.val

        points = (
            result.planned_trajectory
            .joint_trajectory.points
        )

        self.get_logger().info(
            f'MoveIt error code: {error_code}'
        )

        self.get_logger().info(
            f'Planning time: {result.planning_time:.3f} s'
        )

        self.get_logger().info(
            f'Trajectory points: {len(points)}'
        )

        if error_code == 1 and len(points) > 0:

            self.get_logger().info(
                'IK JOINT-SPACE PLANNING SUCCESS!'
            )

            for i, point in enumerate(points):
                self.get_logger().info(
                    f'Point {i}: {list(point.positions)}'
                )

            self.get_logger().info(
                'PLAN ONLY: ROBOT NOT MOVED.'
            )

            return 0

        self.get_logger().error(
            'IK JOINT-SPACE PLANNING FAILED!'
        )

        return 1


def main(args=None):

    rclpy.init(args=args)

    node = IKJointPlanTest()

    try:
        return node.run()

    except KeyboardInterrupt:
        return 130

    except Exception as exc:
        node.get_logger().error(f'Unexpected error: {exc}')
        return 10

    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    sys.exit(main())