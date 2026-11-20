// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robotiq_msgs:msg/GripperStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotiq_msgs/msg/gripper_status.hpp"


#ifndef ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__BUILDER_HPP_
#define ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robotiq_msgs/msg/detail/gripper_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robotiq_msgs
{

namespace msg
{

namespace builder
{

class Init_GripperStatus_gripper_fault_severity
{
public:
  explicit Init_GripperStatus_gripper_fault_severity(::robotiq_msgs::msg::GripperStatus & msg)
  : msg_(msg)
  {}
  ::robotiq_msgs::msg::GripperStatus gripper_fault_severity(::robotiq_msgs::msg::GripperStatus::_gripper_fault_severity_type arg)
  {
    msg_.gripper_fault_severity = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robotiq_msgs::msg::GripperStatus msg_;
};

class Init_GripperStatus_gripper_fault
{
public:
  explicit Init_GripperStatus_gripper_fault(::robotiq_msgs::msg::GripperStatus & msg)
  : msg_(msg)
  {}
  Init_GripperStatus_gripper_fault_severity gripper_fault(::robotiq_msgs::msg::GripperStatus::_gripper_fault_type arg)
  {
    msg_.gripper_fault = std::move(arg);
    return Init_GripperStatus_gripper_fault_severity(msg_);
  }

private:
  ::robotiq_msgs::msg::GripperStatus msg_;
};

class Init_GripperStatus_motor_current
{
public:
  explicit Init_GripperStatus_motor_current(::robotiq_msgs::msg::GripperStatus & msg)
  : msg_(msg)
  {}
  Init_GripperStatus_gripper_fault motor_current(::robotiq_msgs::msg::GripperStatus::_motor_current_type arg)
  {
    msg_.motor_current = std::move(arg);
    return Init_GripperStatus_gripper_fault(msg_);
  }

private:
  ::robotiq_msgs::msg::GripperStatus msg_;
};

class Init_GripperStatus_object_detection
{
public:
  explicit Init_GripperStatus_object_detection(::robotiq_msgs::msg::GripperStatus & msg)
  : msg_(msg)
  {}
  Init_GripperStatus_motor_current object_detection(::robotiq_msgs::msg::GripperStatus::_object_detection_type arg)
  {
    msg_.object_detection = std::move(arg);
    return Init_GripperStatus_motor_current(msg_);
  }

private:
  ::robotiq_msgs::msg::GripperStatus msg_;
};

class Init_GripperStatus_header
{
public:
  Init_GripperStatus_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GripperStatus_object_detection header(::robotiq_msgs::msg::GripperStatus::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_GripperStatus_object_detection(msg_);
  }

private:
  ::robotiq_msgs::msg::GripperStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robotiq_msgs::msg::GripperStatus>()
{
  return robotiq_msgs::msg::builder::Init_GripperStatus_header();
}

}  // namespace robotiq_msgs

#endif  // ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__BUILDER_HPP_
