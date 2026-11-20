# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target robotiq_msgs::robotiq_msgs
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${robotiq_msgs_TARGETS}.
if(robotiq_msgs_TARGETS AND NOT TARGET robotiq_msgs::robotiq_msgs)
  add_library(robotiq_msgs::robotiq_msgs INTERFACE IMPORTED)
  set_target_properties(robotiq_msgs::robotiq_msgs PROPERTIES
    INTERFACE_LINK_LIBRARIES "${robotiq_msgs_TARGETS}")
endif()
