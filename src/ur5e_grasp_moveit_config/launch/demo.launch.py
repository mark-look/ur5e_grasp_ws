from launch import LaunchDescription
from launch_ros.actions import SetParameter

from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import (
    generate_move_group_launch,
    generate_moveit_rviz_launch,
    generate_static_virtual_joint_tfs_launch,
)


def generate_launch_description():

    # ==================================================
    # Load MoveIt configuration
    # ==================================================

    moveit_config = MoveItConfigsBuilder(
        "ur5e_robotiq",
        package_name="ur5e_grasp_moveit_config"
    ).to_moveit_configs()

    ld = LaunchDescription()

    # ==================================================
    # Enable Gazebo simulation time
    # ==================================================

    ld.add_action(
        SetParameter(
            name="use_sim_time",
            value=True
        )
    )

    # ==================================================
    # Static virtual joint TF
    # Keep world -> base_link if defined in SRDF
    # ==================================================

    virtual_joint_launch = (
        generate_static_virtual_joint_tfs_launch(moveit_config)
    )

    for action in virtual_joint_launch.entities:
        ld.add_action(action)

    # ==================================================
    # MoveIt move_group
    # No robot_state_publisher
    # No ros2_control_node
    # No controller spawners
    # ==================================================

    move_group_launch = generate_move_group_launch(
        moveit_config
    )

    for action in move_group_launch.entities:
        ld.add_action(action)

    # ==================================================
    # RViz
    # ==================================================

    rviz_launch = generate_moveit_rviz_launch(
        moveit_config
    )

    for action in rviz_launch.entities:
        ld.add_action(action)

    return ld