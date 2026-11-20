// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robotiq_msgs:msg/GripperStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotiq_msgs/msg/gripper_status.h"


#ifndef ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__STRUCT_H_
#define ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Constant 'MOVING'.
/**
  * gOBJ. The gripper's own answer to "am I holding something", and the only
  * authoritative one: a stall flag or a position comparison is a guess at this.
 */
enum
{
  robotiq_msgs__msg__GripperStatus__MOVING = 0
};

/// Constant 'DETECTED_WHILE_OPENING'.
enum
{
  robotiq_msgs__msg__GripperStatus__DETECTED_WHILE_OPENING = 1
};

/// Constant 'DETECTED_WHILE_CLOSING'.
enum
{
  robotiq_msgs__msg__GripperStatus__DETECTED_WHILE_CLOSING = 2
};

/// Constant 'AT_REQUESTED_POSITION'.
enum
{
  robotiq_msgs__msg__GripperStatus__AT_REQUESTED_POSITION = 3
};

/// Constant 'GRIPPER_FAULT_UNKNOWN'.
/**
  * gFLT, as the instruction manual numbers it. The register is four bits wide, so
  * a code the manual does not list can still arrive: treat it as an undefined
  * fault, which gripper_fault_severity reports as major.
  *
  * UNKNOWN is outside the register, and says the gripper did not report a fault
  * this cycle, either because the hardware exports no fault interface or because
  * the reading failed. It is not NONE: an unfaulted gripper and a gripper that
  * is not reporting a fault state are different, and only one of them is safe to act on.
 */
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_UNKNOWN = 255
};

/// Constant 'GRIPPER_FAULT_NONE'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_NONE = 0
};

/// Constant 'GRIPPER_FAULT_ACTION_DELAYED'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_ACTION_DELAYED = 5
};

/// Constant 'GRIPPER_FAULT_ACTIVATION_REQUIRED'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_ACTIVATION_REQUIRED = 7
};

/// Constant 'GRIPPER_FAULT_OVER_TEMPERATURE'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_OVER_TEMPERATURE = 8
};

/// Constant 'GRIPPER_FAULT_NO_COMMUNICATION'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_NO_COMMUNICATION = 9
};

/// Constant 'GRIPPER_FAULT_UNDER_VOLTAGE'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_UNDER_VOLTAGE = 10
};

/// Constant 'GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS = 11
};

/// Constant 'GRIPPER_FAULT_INTERNAL_FAULT'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_INTERNAL_FAULT = 12
};

/// Constant 'GRIPPER_FAULT_ACTIVATION_FAULT'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_ACTIVATION_FAULT = 13
};

/// Constant 'GRIPPER_FAULT_OVERCURRENT'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_OVERCURRENT = 14
};

/// Constant 'GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE = 15
};

/// Constant 'GRIPPER_FAULT_SEVERITY_UNKNOWN'.
/**
  * How bad the gripper fault is. A major fault clears only on a reactivation;
  * the manual calls the warning tier "priority faults". UNKNOWN accompanies
  * GRIPPER_FAULT_UNKNOWN: the two fields are exported together or not at all.
 */
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_SEVERITY_UNKNOWN = 255
};

/// Constant 'GRIPPER_FAULT_SEVERITY_NONE'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_SEVERITY_NONE = 0
};

/// Constant 'GRIPPER_FAULT_SEVERITY_WARNING'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_SEVERITY_WARNING = 1
};

/// Constant 'GRIPPER_FAULT_SEVERITY_MINOR'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_SEVERITY_MINOR = 2
};

/// Constant 'GRIPPER_FAULT_SEVERITY_MAJOR'.
enum
{
  robotiq_msgs__msg__GripperStatus__GRIPPER_FAULT_SEVERITY_MAJOR = 3
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/GripperStatus in the package robotiq_msgs.
/**
  * What the gripper reports about itself, decoded. The driver reads these out of
  * the status block every exchange cycle; a broadcaster republishes them here so
  * that a client off the controller manager can read them without re-deriving
  * anything from a register.
 */
typedef struct robotiq_msgs__msg__GripperStatus
{
  std_msgs__msg__Header header;
  uint8_t object_detection;
  /// gCU in amperes. Motor current, not grip force, and not convertible to one.
  double motor_current;
  uint8_t gripper_fault;
  uint8_t gripper_fault_severity;
} robotiq_msgs__msg__GripperStatus;

// Struct for a sequence of robotiq_msgs__msg__GripperStatus.
typedef struct robotiq_msgs__msg__GripperStatus__Sequence
{
  robotiq_msgs__msg__GripperStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robotiq_msgs__msg__GripperStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOTIQ_MSGS__MSG__DETAIL__GRIPPER_STATUS__STRUCT_H_
