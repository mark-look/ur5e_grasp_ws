#!/usr/bin/env python3

from launch import LaunchDescription

from launch.actions import (
    DeclareLaunchArgument,
    ExecuteProcess,
    IncludeLaunchDescription,
    LogInfo,
    SetEnvironmentVariable,
    TimerAction,
)

from launch.conditions import IfCondition

from launch.launch_description_sources import (
    PythonLaunchDescriptionSource
)

from launch.substitutions import (
    LaunchConfiguration,
    PathJoinSubstitution
)

from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # ==========================================
    # 1. Launch 参数
    # ==========================================

    start_gazebo = LaunchConfiguration(
        'start_gazebo'
    )

    start_moveit = LaunchConfiguration(
        'start_moveit'
    )

    open_gripper = LaunchConfiguration(
        'open_gripper'
    )

    execute_alignment = LaunchConfiguration(
        'execute_alignment'
    )

    startup_delay = LaunchConfiguration(
        'startup_delay'
    )

    # ==========================================
    # 2. 获取功能包路径
    # ==========================================

    description_share = FindPackageShare(
        'ur5e_grasp_description'
    )

    moveit_share = FindPackageShare(
        'ur5e_grasp_moveit_config'
    )

    # ==========================================
    # 3. 启动 Gazebo
    # ==========================================

    gazebo_launch = IncludeLaunchDescription(

        PythonLaunchDescriptionSource(

            PathJoinSubstitution([
                description_share,
                'launch',
                'gazebo.launch.py'
            ])

        ),

        condition=IfCondition(start_gazebo)
    )

    # ==========================================
    # 4. 启动 MoveIt + RViz
    # ==========================================

    moveit_launch = IncludeLaunchDescription(

        PythonLaunchDescriptionSource(

            PathJoinSubstitution([
                moveit_share,
                'launch',
                'demo.launch.py'
            ])

        ),

        condition=IfCondition(start_moveit)
    )

    # ==========================================
    # 5. 仿真场景初始化脚本
    # ==========================================

    setup_script = r'''
set -Eeuo pipefail

source /opt/ros/jazzy/setup.bash
source "$HOME/ur5e_grasp_ws/install/setup.bash"

WS="$HOME/ur5e_grasp_ws/src/ur5e_grasp_description"

TABLE="$WS/models/table/table.sdf"
BALL="$WS/models/red_ball/red_ball.sdf"

SCENE="$WS/scripts/add_grasp_scene.py"
ALIGN="$WS/scripts/execute_pregrasp.py"

echo ""
echo "========================================"
echo " UR5e GRASP WORKFLOW"
echo "========================================"

# ==========================================
# 5.1 检查文件
# ==========================================

for f in "$TABLE" "$BALL" "$SCENE"; do

    if [[ ! -f "$f" ]]; then

        echo "ERROR: File not found: $f"

        exit 1

    fi

done

# ==========================================
# 5.2 等待 Gazebo World
# ==========================================

echo ""
echo "[1/6] Waiting for Gazebo..."

WORLD_READY=false

for i in $(seq 1 90); do

    if gz service -l 2>/dev/null \
        | grep -q '^/world/empty/create$'; then

        WORLD_READY=true
        break

    fi

    sleep 1

done

if [[ "$WORLD_READY" != "true" ]]; then

    echo "ERROR: Gazebo world unavailable!"

    exit 1

fi

echo "Gazebo World: empty READY"

# ==========================================
# 5.3 检查桌子
# ==========================================

MODEL_LIST=$(gz model --list)

if echo "$MODEL_LIST" | grep -Eq \
    '^[[:space:]]*-[[:space:]]+table$'; then

    echo "Table already exists."

else

    echo "Creating table..."

    ros2 run ros_gz_sim create \
        -world empty \
        -file "$TABLE" \
        -name table \
        -x 0.5 \
        -y 0.0 \
        -z 0.0

fi

# ==========================================
# 5.4 检查红球
# ==========================================

MODEL_LIST=$(gz model --list)

if echo "$MODEL_LIST" | grep -Eq \
    '^[[:space:]]*-[[:space:]]+red_ball$'; then

    echo "Red ball already exists."

else

    echo "Creating red ball..."

    ros2 run ros_gz_sim create \
        -world empty \
        -file "$BALL" \
        -name red_ball \
        -x 0.5 \
        -y 0.0 \
        -z 0.46

fi

# ==========================================
# 5.5 检查模型位置
# ==========================================

echo ""
echo "===== GAZEBO TABLE ====="

gz model -m table --pose

echo ""
echo "===== GAZEBO RED BALL ====="

gz model -m red_ball --pose

# ==========================================
# 5.6 等待 MoveIt
# ==========================================

echo ""
echo "[2/6] Waiting for MoveIt..."

SERVICE_READY=false

for i in $(seq 1 90); do

    if ros2 service list 2>/dev/null \
        | grep -qx '/apply_planning_scene'; then

        SERVICE_READY=true
        break

    fi

    sleep 1

done

if [[ "$SERVICE_READY" != "true" ]]; then

    echo "ERROR: MoveIt service unavailable!"

    exit 1

fi

echo "MoveIt READY"

# ==========================================
# 5.7 加载碰撞场景
# ==========================================

echo ""
echo "[3/6] Loading MoveIt collision scene..."

python3 "$SCENE"

echo "Planning scene loaded."

# ==========================================
# 5.8 打开 Robotiq 夹爪
# ==========================================

if [[ "${OPEN_GRIPPER}" == "true" ]]; then

    echo ""
    echo "[4/6] Waiting for gripper controller..."

    GRIPPER_READY=false

    for i in $(seq 1 60); do

        if ros2 action list 2>/dev/null \
            | grep -qx \
            '/robotiq_gripper_controller/follow_joint_trajectory'; then

            GRIPPER_READY=true
            break

        fi

        sleep 1

    done

    if [[ "$GRIPPER_READY" != "true" ]]; then

        echo "ERROR: Gripper controller unavailable!"

        exit 1

    fi

    echo "Opening Robotiq 2F-85..."

    ros2 action send_goal \
        /robotiq_gripper_controller/follow_joint_trajectory \
        control_msgs/action/FollowJointTrajectory \
        "{trajectory: {joint_names: [robotiq_85_left_knuckle_joint], points: [{positions: [0.0], time_from_start: {sec: 3, nanosec: 0}}]}}"

fi

# ==========================================
# 5.9 可选：水平对准运动
# ==========================================

if [[ "${EXECUTE_ALIGNMENT}" == "true" ]]; then

    echo ""
    echo "[5/6] Executing horizontal alignment..."

    if [[ ! -f "$ALIGN" ]]; then

        echo "ERROR: Alignment script unavailable!"

        exit 1

    fi

    echo "Check execute_pregrasp.py target joints first."

    printf '\n' | python3 "$ALIGN"

else

    echo ""
    echo "[5/6] Horizontal alignment skipped."

fi

# ==========================================
# 5.10 完成
# ==========================================

echo ""
echo "========================================"
echo " GRASP WORKFLOW INITIALIZATION COMPLETE"
echo "========================================"

echo ""
echo "Completed:"

echo "1. Gazebo started."
echo "2. MoveIt started."
echo "3. Table checked."
echo "4. Red ball checked."
echo "5. Collision scene loaded."
echo "6. Robotiq gripper opened."

echo ""
echo "Next operations:"

echo "1. Verify robot current state."
echo "2. Execute horizontal alignment if needed."
echo "3. Check 5mm descent endpoint collision."
echo "4. Execute 5mm descent."
echo "5. Measure fingertip positions."
echo "6. Plan gripper closing."
echo "7. Attach red ball."
echo "8. Lift and place red ball."

echo ""
echo "IMPORTANT:"
echo "Descent and grasp are NOT automatic."

echo "========================================"

'''

    setup_process = ExecuteProcess(

        cmd=[
            'bash',
            '-lc',
            setup_script
        ],

        additional_env={

            'OPEN_GRIPPER': open_gripper,

            'EXECUTE_ALIGNMENT': execute_alignment,

            'LIBGL_ALWAYS_SOFTWARE': '1',

        },

        output='screen',

        name='grasp_workflow_setup'
    )

    # ==========================================
    # 6. 返回 Launch Description
    # ==========================================

    return LaunchDescription([

        DeclareLaunchArgument(

            'start_gazebo',

            default_value='true',

            description='Start Gazebo simulation'
        ),

        DeclareLaunchArgument(

            'start_moveit',

            default_value='true',

            description='Start MoveIt and RViz'
        ),

        DeclareLaunchArgument(

            'open_gripper',

            default_value='true',

            description='Open Robotiq 2F-85'
        ),

        DeclareLaunchArgument(

            'execute_alignment',

            default_value='false',

            description='Execute horizontal alignment automatically'
        ),

        DeclareLaunchArgument(

            'startup_delay',

            default_value='10.0',

            description='Initial delay before scene setup'
        ),

        SetEnvironmentVariable(
            'LIBGL_ALWAYS_SOFTWARE',
            '1'
        ),

        LogInfo(
            msg='Starting UR5e Grasp Workflow...'
        ),

        gazebo_launch,

        moveit_launch,

        TimerAction(

            period=startup_delay,

            actions=[
                setup_process
            ]

        ),

    ])