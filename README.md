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