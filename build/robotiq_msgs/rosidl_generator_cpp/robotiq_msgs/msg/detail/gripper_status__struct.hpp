// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robotiq_msgs:msg/GripperStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotiq_msgs/msg/gripper_status.hpp"


#ifndef ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__STRUCT_HPP_
#define ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robotiq_msgs__msg__GripperStatus __attribute__((deprecated))
#else
# define DEPRECATED__robotiq_msgs__msg__GripperStatus __declspec(deprecated)
#endif

namespace robotiq_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct GripperStatus_
{
  using Type = GripperStatus_<ContainerAllocator>;

  explicit GripperStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->gripper_fault = 255;
      this->gripper_fault_severity = 255;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->object_detection = 0;
      this->motor_current = 0.0;
      this->gripper_fault = 0;
      this->gripper_fault_severity = 0;
    }
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->object_detection = 0;
      this->motor_current = 0.0;
    }
  }

  explicit GripperStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->gripper_fault = 255;
      this->gripper_fault_severity = 255;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->object_detection = 0;
      this->motor_current = 0.0;
      this->gripper_fault = 0;
      this->gripper_fault_severity = 0;
    }
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->object_detection = 0;
      this->motor_current = 0.0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _object_detection_type =
    uint8_t;
  _object_detection_type object_detection;
  using _motor_current_type =
    double;
  _motor_current_type motor_current;
  using _gripper_fault_type =
    uint8_t;
  _gripper_fault_type gripper_fault;
  using _gripper_fault_severity_type =
    uint8_t;
  _gripper_fault_severity_type gripper_fault_severity;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__object_detection(
    const uint8_t & _arg)
  {
    this->object_detection = _arg;
    return *this;
  }
  Type & set__motor_current(
    const double & _arg)
  {
    this->motor_current = _arg;
    return *this;
  }
  Type & set__gripper_fault(
    const uint8_t & _arg)
  {
    this->gripper_fault = _arg;
    return *this;
  }
  Type & set__gripper_fault_severity(
    const uint8_t & _arg)
  {
    this->gripper_fault_severity = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t MOVING =
    0u;
  static constexpr uint8_t DETECTED_WHILE_OPENING =
    1u;
  static constexpr uint8_t DETECTED_WHILE_CLOSING =
    2u;
  static constexpr uint8_t AT_REQUESTED_POSITION =
    3u;
  static constexpr uint8_t GRIPPER_FAULT_UNKNOWN =
    255u;
  static constexpr uint8_t GRIPPER_FAULT_NONE =
    0u;
  static constexpr uint8_t GRIPPER_FAULT_ACTION_DELAYED =
    5u;
  static constexpr uint8_t GRIPPER_FAULT_ACTIVATION_REQUIRED =
    7u;
  static constexpr uint8_t GRIPPER_FAULT_OVER_TEMPERATURE =
    8u;
  static constexpr uint8_t GRIPPER_FAULT_NO_COMMUNICATION =
    9u;
  static constexpr uint8_t GRIPPER_FAULT_UNDER_VOLTAGE =
    10u;
  static constexpr uint8_t GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS =
    11u;
  static constexpr uint8_t GRIPPER_FAULT_INTERNAL_FAULT =
    12u;
  static constexpr uint8_t GRIPPER_FAULT_ACTIVATION_FAULT =
    13u;
  static constexpr uint8_t GRIPPER_FAULT_OVERCURRENT =
    14u;
  static constexpr uint8_t GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE =
    15u;
  static constexpr uint8_t GRIPPER_FAULT_SEVERITY_UNKNOWN =
    255u;
  static constexpr uint8_t GRIPPER_FAULT_SEVERITY_NONE =
    0u;
  static constexpr uint8_t GRIPPER_FAULT_SEVERITY_WARNING =
    1u;
  static constexpr uint8_t GRIPPER_FAULT_SEVERITY_MINOR =
    2u;
  static constexpr uint8_t GRIPPER_FAULT_SEVERITY_MAJOR =
    3u;

  // pointer types
  using RawPtr =
    robotiq_msgs::msg::GripperStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const robotiq_msgs::msg::GripperStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robotiq_msgs::msg::GripperStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robotiq_msgs::msg::GripperStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robotiq_msgs::msg::GripperStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robotiq_msgs::msg::GripperStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robotiq_msgs::msg::GripperStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robotiq_msgs::msg::GripperStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robotiq_msgs::msg::GripperStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robotiq_msgs::msg::GripperStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robotiq_msgs__msg__GripperStatus
    std::shared_ptr<robotiq_msgs::msg::GripperStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robotiq_msgs__msg__GripperStatus
    std::shared_ptr<robotiq_msgs::msg::GripperStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GripperStatus_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->object_detection != other.object_detection) {
      return false;
    }
    if (this->motor_current != other.motor_current) {
      return false;
    }
    if (this->gripper_fault != other.gripper_fault) {
      return false;
    }
    if (this->gripper_fault_severity != other.gripper_fault_severity) {
      return false;
    }
    return true;
  }
  bool operator!=(const GripperStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GripperStatus_

// alias to use template instance with default allocator
using GripperStatus =
  robotiq_msgs::msg::GripperStatus_<std::allocator<void>>;

// constant definitions
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::MOVING;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::DETECTED_WHILE_OPENING;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::DETECTED_WHILE_CLOSING;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::AT_REQUESTED_POSITION;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_UNKNOWN;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_NONE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_ACTION_DELAYED;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_ACTIVATION_REQUIRED;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_OVER_TEMPERATURE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_NO_COMMUNICATION;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_UNDER_VOLTAGE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_INTERNAL_FAULT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_ACTIVATION_FAULT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_OVERCURRENT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_SEVERITY_UNKNOWN;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_SEVERITY_NONE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_SEVERITY_WARNING;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_SEVERITY_MINOR;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t GripperStatus_<ContainerAllocator>::GRIPPER_FAULT_SEVERITY_MAJOR;
#endif  // __cplusplus < 201703L

}  // namespace msg

}  // namespace robotiq_msgs

#endif  // ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__STRUCT_HPP_
