<!-- 只编译目标包 -->
cd ur5e_grasp_ws
source /opt/ros/jazzy/setup.bash

colcon build \
  --packages-select ur5e_grasp_description \
  --packages-ignore \
    robotiq_controllers \
    robotiq_driver \
    robotiq_msgs \
    robotiq_grippers_sdk_vendor \
  --symlink-install

<!-- 软件渲染 -->
source /opt/ros/jazzy/setup.bash
source install/setup.bash

export GZ_SIM_PHYSICS_ENGINE_PATH=/opt/ros/jazzy/opt/gz_physics_vendor/lib/gz-physics-7/engine-plugins

LIBGL_ALWAYS_SOFTWARE=1 ros2 launch ur5e_grasp_description gazebo.launch.py

<!-- 若出现问题，可检查时钟问题 -->


<!-- 启动桌子 -->
cd ~/ur5e_grasp_ws

source /opt/ros/jazzy/setup.bash
source install/setup.bash

ros2 run ros_gz_sim create \
  -world empty \
  -file src/ur5e_grasp_description/models/table/table.sdf \
  -name table \
  -x 0.5 -y 0 -z 0
<!-- 启动球 -->
ros2 run ros_gz_sim create \
  -world empty \
  -file src/ur5e_grasp_description/models/red_ball/red_ball.sdf \
  -name red_ball \
  -x 0.5 -y 0 -z 0.46

<!-- 启动rviz2 -->
cd ~/ur5e_grasp_ws
source /opt/ros/jazzy/setup.bash
source install/setup.bash

ros2 launch ur5e_grasp_moveit_config demo.launch.py

<!-- 在rviz中显示桌子与球 -->
cd ~/ur5e_grasp_ws
source /opt/ros/jazzy/setup.bash
source install/setup.bash

python3 src/ur5e_grasp_description/scripts/add_grasp_scene.py

<!-- chatgpt总结的步骤(总结欲抓取的步骤) -->
<!-- 终端 1：Gazebo -->
cd ~/ur5e_grasp_ws

source /opt/ros/jazzy/setup.bash
source install/setup.bash

export LIBGL_ALWAYS_SOFTWARE=1

ros2 launch ur5e_grasp_description gazebo.launch.py
<!-- 终端 2：MoveIt -->
cd ~/ur5e_grasp_ws

source /opt/ros/jazzy/setup.bash
source install/setup.bash

export LIBGL_ALWAYS_SOFTWARE=1

ros2 launch ur5e_grasp_moveit_config demo.launch.py
<!-- 终端 3：生成桌子和红球 -->
cd ~/ur5e_grasp_ws

source /opt/ros/jazzy/setup.bash
source install/setup.bash

ros2 run ros_gz_sim create \
-world empty \
-file ~/ur5e_grasp_ws/src/ur5e_grasp_description/models/table/table.sdf \
-name table \
-x 0.5 -y 0.0 -z 0.0

ros2 run ros_gz_sim create \
-world empty \
-file ~/ur5e_grasp_ws/src/ur5e_grasp_description/models/red_ball/red_ball.sdf \
-name red_ball \
-x 0.5 -y 0.0 -z 0.46

python3 ~/ur5e_grasp_ws/src/ur5e_grasp_description/scripts/add_grasp_scene.py

gz model --list
<!-- 执行预抓取程序 -->
python3 ~/ur5e_grasp_ws/src/ur5e_grasp_description/scripts/execute_pregrasp.py