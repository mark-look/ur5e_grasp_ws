from launch import LaunchDescription
from launch_ros.actions import SetParameter

from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch


def generate_launch_description():

    moveit_config = MoveItConfigsBuilder(
        "ur5e_robotiq",
        package_name="ur5e_grasp_moveit_config"
    ).to_moveit_configs()

    # Enable Gazebo simulation time before starting MoveGroup
    ld = LaunchDescription()

    ld.add_action(
        SetParameter(
            name="use_sim_time",
            value=True
        )
    )

    move_group_launch = generate_move_group_launch(moveit_config)

    for action in move_group_launch.entities:
        ld.add_action(action)

    return ld