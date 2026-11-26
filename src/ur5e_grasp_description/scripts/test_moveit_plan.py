#!/usr/bin/env python3

import sys
import rclpy

from rclpy.node import Node
from rclpy.action import ActionClient

from moveit_msgs.action import MoveGroup
from moveit_msgs.msg import Constraints, JointConstraint


class MoveItPlanTest(Node):

    def __init__(self):
        super().__init__("moveit_plan_test")

        self.client = ActionClient(
            self,
            MoveGroup,
            "/move_action"
        )

    def run(self):

        self.get_logger().info("Waiting for MoveGroup action...")

        if not self.client.wait_for_server(timeout_sec=30.0):
            self.get_logger().error("MoveGroup action server unavailable!")
            return 1

        # ==========================================
        # Create MoveGroup request
        # ==========================================

        goal = MoveGroup.Goal()
        request = goal.request

        request.group_name = "ur_manipulator"
        request.pipeline_id = "ompl"
        request.planner_id = ""

        request.num_planning_attempts = 5
        request.allowed_planning_time = 10.0

        request.max_velocity_scaling_factor = 0.05
        request.max_acceleration_scaling_factor = 0.05

        request.start_state.is_diff = True

        # ==========================================
        # Small joint movement target
        # ==========================================

        target_positions = {
            "shoulder_pan_joint": 0.02,
            "shoulder_lift_joint": -1.55,
            "elbow_joint": 0.02,
            "wrist_1_joint": -1.55,
            "wrist_2_joint": -0.02,
            "wrist_3_joint": 0.02,
        }

        constraints = Constraints()
        constraints.name = "ur5e_safe_execution_test"

        for joint_name, position in target_positions.items():

            joint_constraint = JointConstraint()

            joint_constraint.joint_name = joint_name
            joint_constraint.position = position
            joint_constraint.tolerance_above = 0.01
            joint_constraint.tolerance_below = 0.01
            joint_constraint.weight = 1.0

            constraints.joint_constraints.append(joint_constraint)

        request.goal_constraints = [constraints]

        # ==========================================
        # IMPORTANT: Execute trajectory
        # ==========================================

        goal.planning_options.plan_only = False
        goal.planning_options.replan = False

        self.get_logger().info("====================================")
        self.get_logger().info("UR5e PLANNING + EXECUTION TEST")
        self.get_logger().info("Group: ur_manipulator")
        self.get_logger().info("Pipeline: ompl")
        self.get_logger().info("Velocity scaling: 0.05")
        self.get_logger().info("Acceleration scaling: 0.05")
        self.get_logger().info("Execution: ENABLED")
        self.get_logger().info("====================================")

        self.get_logger().warn(
            "The robot will move. Keep the simulated workspace clear."
        )

        input("Press ENTER to start execution, or Ctrl+C to cancel...")

        # ==========================================
        # Send goal
        # ==========================================

        send_future = self.client.send_goal_async(goal)

        rclpy.spin_until_future_complete(
            self,
            send_future,
            timeout_sec=35.0
        )

        if not send_future.done():
            self.get_logger().error("Timeout waiting for planning request!")
            return 1

        goal_handle = send_future.result()

        if goal_handle is None or not goal_handle.accepted:
            self.get_logger().error("MoveIt request rejected!")
            return 1

        self.get_logger().info("MoveIt request accepted.")

        # ==========================================
        # Get execution result
        # ==========================================

        result_future = goal_handle.get_result_async()

        rclpy.spin_until_future_complete(
            self,
            result_future,
            timeout_sec=90.0
        )

        if not result_future.done():
            self.get_logger().error("Timeout waiting for execution result!")
            return 1

        wrapped_result = result_future.result()

        if wrapped_result is None:
            self.get_logger().error("No result returned!")
            return 1

        result = wrapped_result.result
        error_code = result.error_code.val

        self.get_logger().info(f"MoveIt error code: {error_code}")
        self.get_logger().info(
            f"Planning time: {result.planning_time:.3f} seconds"
        )

        self.get_logger().info(
            f"Trajectory joints: "
            f"{result.planned_trajectory.joint_trajectory.joint_names}"
        )

        self.get_logger().info(
            f"Trajectory points: "
            f"{len(result.planned_trajectory.joint_trajectory.points)}"
        )

        # ==========================================
        # Result
        # ==========================================

        if error_code == 1:

            self.get_logger().info("====================================")
            self.get_logger().info("EXECUTION SUCCESS!")
            self.get_logger().info("MoveIt returned SUCCESS.")
            self.get_logger().info("====================================")

            return 0

        self.get_logger().error("====================================")
        self.get_logger().error("EXECUTION FAILED!")
        self.get_logger().error(f"MoveIt error code: {error_code}")
        self.get_logger().error("====================================")

        return 1


def main(args=None):

    rclpy.init(args=args)

    node = MoveItPlanTest()

    try:
        exit_code = node.run()

    except KeyboardInterrupt:
        exit_code = 130

    except Exception as exc:
        node.get_logger().error(f"Unexpected error: {exc}")
        exit_code = 10

    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()

    return exit_code


if __name__ == "__main__":
    sys.exit(main())