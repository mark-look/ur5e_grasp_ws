import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    # ==================================================
    # Robotiq mesh resource path
    # ==================================================

    robotiq_share_path = os.path.expanduser(
        "~/ur5e_grasp_ws/install/robotiq_description/share"
    )

    current_resource_path = os.environ.get(
        "GZ_SIM_RESOURCE_PATH", ""
    )

    resource_paths = [
        path for path in current_resource_path.split(os.pathsep)
        if path
    ]

    if robotiq_share_path not in resource_paths:
        resource_paths.append(robotiq_share_path)

    os.environ["GZ_SIM_RESOURCE_PATH"] = os.pathsep.join(
        resource_paths
    )

    print(
        "[Gazebo] GZ_SIM_RESOURCE_PATH = "
        + os.environ["GZ_SIM_RESOURCE_PATH"]
    )

    # ==================================================
    # Robot description
    # ==================================================

    robot_description_content = Command(
        [
            FindExecutable(name="xacro"),
            " ",
            PathJoinSubstitution(
                [
                    FindPackageShare("ur5e_grasp_description"),
                    "urdf",
                    "ur5e_robotiq.urdf.xacro",
                ]
            ),
        ]
    )

    robot_description = {
        "robot_description": ParameterValue(
            robot_description_content,
            value_type=str
        )
    }

    # ==================================================
    # Robot state publisher
    # ==================================================

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[
            robot_description,
            {"use_sim_time": True},
        ],
    )

    # ==================================================
    # Gazebo Harmonic
    # ==================================================

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    FindPackageShare("ros_gz_sim"),
                    "launch",
                    "gz_sim.launch.py",
                ]
            )
        ),
        launch_arguments={
            "gz_args": "-r -v 3 --physics-engine gz-physics-bullet-featherstone-plugin empty.sdf"
        }.items(),
    )

    # ==================================================
    # Bridge Gazebo simulation clock to ROS 2
    # ==================================================

    clock_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock"
        ],
        output="screen",
    )

    # ==================================================
    # Spawn robot into Gazebo
    # ==================================================

    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=[
            "-topic",
            "robot_description",
            "-name",
            "ur5e_robotiq",
        ],
    )

    # ==================================================
    # Joint state broadcaster
    # ==================================================

    joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
        ],
        output="screen",
    )

    # ==================================================
    # UR5e arm controller
    # ==================================================

    arm_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "ur5e_arm_controller",
            "--controller-manager",
            "/controller_manager",
        ],
        output="screen",
    )

    # ==================================================
    # Robotiq gripper controller
    # ==================================================

    gripper_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "robotiq_gripper_controller",
            "--controller-manager",
            "/controller_manager",
        ],
        output="screen",
    )

    # ==================================================
    # Launch description
    # ==================================================

    return LaunchDescription(
        [
            gazebo,
            clock_bridge,
            robot_state_publisher,
            spawn_robot,

            RegisterEventHandler(
                OnProcessExit(
                    target_action=spawn_robot,
                    on_exit=[joint_state_broadcaster],
                )
            ),

            RegisterEventHandler(
                OnProcessExit(
                    target_action=joint_state_broadcaster,
                    on_exit=[arm_controller],
                )
            ),

            RegisterEventHandler(
                OnProcessExit(
                    target_action=arm_controller,
                    on_exit=[gripper_controller],
                )
            ),
        ]
    )