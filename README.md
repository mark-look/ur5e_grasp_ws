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
  -x 0.5 -y 0 -z 0.85

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