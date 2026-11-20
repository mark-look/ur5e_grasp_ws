// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robotiq_msgs:msg/GripperStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotiq_msgs/msg/gripper_status.hpp"


#ifndef ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__TRAITS_HPP_
#define ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robotiq_msgs/msg/detail/gripper_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace robotiq_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const GripperStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: object_detection
  {
    out << "object_detection: ";
    rosidl_generator_traits::value_to_yaml(msg.object_detection, out);
    out << ", ";
  }

  // member: motor_current
  {
    out << "motor_current: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_current, out);
    out << ", ";
  }

  // member: gripper_fault
  {
    out << "gripper_fault: ";
    rosidl_generator_traits::value_to_yaml(msg.gripper_fault, out);
    out << ", ";
  }

  // member: gripper_fault_severity
  {
    out << "gripper_fault_severity: ";
    rosidl_generator_traits::value_to_yaml(msg.gripper_fault_severity, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GripperStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: object_detection
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "object_detection: ";
    rosidl_generator_traits::value_to_yaml(msg.object_detection, out);
    out << "\n";
  }

  // member: motor_current
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor_current: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_current, out);
    out << "\n";
  }

  // member: gripper_fault
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gripper_fault: ";
    rosidl_generator_traits::value_to_yaml(msg.gripper_fault, out);
    out << "\n";
  }

  // member: gripper_fault_severity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gripper_fault_severity: ";
    rosidl_generator_traits::value_to_yaml(msg.gripper_fault_severity, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GripperStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace robotiq_msgs

namespace rosidl_generator_traits
{

[[deprecated("use robotiq_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robotiq_msgs::msg::GripperStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  robotiq_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robotiq_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const robotiq_msgs::msg::GripperStatus & msg)
{
  return robotiq_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<robotiq_msgs::msg::GripperStatus>()
{
  return "robotiq_msgs::msg::GripperStatus";
}

template<>
inline const char * name<robotiq_msgs::msg::GripperStatus>()
{
  return "robotiq_msgs/msg/GripperStatus";
}

template<>
struct has_fixed_size<robotiq_msgs::msg::GripperStatus>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<robotiq_msgs::msg::GripperStatus>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<robotiq_msgs::msg::GripperStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__TRAITS_HPP_
