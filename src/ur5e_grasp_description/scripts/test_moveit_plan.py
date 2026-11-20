#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from moveit_msgs.action import MoveGroup
from moveit_msgs.msg import Constraints, JointConstraint


class MoveItExecuteTest(Node):

    def __init__(self):
        super().__init__('moveit_execute_test')

        self.client = ActionClient(
            self,
            MoveGroup,
            '/move_action'
        )

        self.get_logger().info('Waiting for MoveGroup action...')

        if not self.client.wait_for_server(timeout_sec=10.0):
            self.get_logger().error(
                'MoveGroup action server unavailable'
            )
            rclpy.shutdown()
            return

        goal = MoveGroup.Goal()

        # 机械臂规划组
        goal.request.group_name = 'ur_manipulator'

        # 使用 OMPL 规划器
        goal.request.pipeline_id = 'ompl'
        goal.request.planner_id = 'RRTConnectkConfigDefault'

        # 规划参数
        goal.request.num_planning_attempts = 10
        goal.request.allowed_planning_time = 10.0

        # 速度和加速度比例
        goal.request.max_velocity_scaling_factor = 0.1
        goal.request.max_acceleration_scaling_factor = 0.1

        # 使用当前机械臂状态作为起始状态
        goal.request.start_state.is_diff = True

        # 设置目标关节约束
        constraints = Constraints()

        joint_names = [
            'shoulder_pan_joint',
            'shoulder_lift_joint',
            'elbow_joint',
            'wrist_1_joint',
            'wrist_2_joint',
            'wrist_3_joint'
        ]

        positions = [
            0.2,
            -0.5,
            0.8,
            -0.3,
            -1.2,
            0.2
        ]

        for name, position in zip(joint_names, positions):

            jc = JointConstraint()

            jc.joint_name = name
            jc.position = position

            jc.tolerance_above = 0.01
            jc.tolerance_below = 0.01
            jc.weight = 1.0

            constraints.joint_constraints.append(jc)

        goal.request.goal_constraints.append(constraints)

        # 关键：False 表示规划后执行
        goal.planning_options.plan_only = False

        goal.planning_options.planning_scene_diff.is_diff = True

        self.get_logger().info(
            'Sending planning and execution request...'
        )

        future = self.client.send_goal_async(goal)

        future.add_done_callback(
            self.goal_response_callback
        )

    def goal_response_callback(self, future):

        handle = future.result()

        if not handle.accepted:

            self.get_logger().error(
                'Planning request rejected'
            )

            rclpy.shutdown()
            return

        self.get_logger().info(
            'Planning request accepted'
        )

        future = handle.get_result_async()

        future.add_done_callback(
            self.result_callback
        )

    def result_callback(self, future):

        result = future.result().result

        error_code = result.error_code.val

        self.get_logger().info(
            f'Error code: {error_code}'
        )

        self.get_logger().info(
            f'Planning time: {result.planning_time:.3f} seconds'
        )

        if error_code == 1:

            self.get_logger().info(
                'SUCCESS: Planning and execution completed!'
            )

        else:

            self.get_logger().error(
                'FAILED: Planning or execution failed!'
            )

        rclpy.shutdown()


def main():

    rclpy.init()

    node = MoveItExecuteTest()

    rclpy.spin(node)


if __name__ == '__main__':
    main()