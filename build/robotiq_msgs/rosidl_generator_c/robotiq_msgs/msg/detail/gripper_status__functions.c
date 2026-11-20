// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robotiq_msgs:msg/GripperStatus.idl
// generated code does not contain a copyright notice
#include "robotiq_msgs/msg/detail/gripper_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
robotiq_msgs__msg__GripperStatus__init(robotiq_msgs__msg__GripperStatus * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    robotiq_msgs__msg__GripperStatus__fini(msg);
    return false;
  }
  // object_detection
  // motor_current
  // gripper_fault
  msg->gripper_fault = 255;
  // gripper_fault_severity
  msg->gripper_fault_severity = 255;
  return true;
}

void
robotiq_msgs__msg__GripperStatus__fini(robotiq_msgs__msg__GripperStatus * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // object_detection
  // motor_current
  // gripper_fault
  // gripper_fault_severity
}

bool
robotiq_msgs__msg__GripperStatus__are_equal(const robotiq_msgs__msg__GripperStatus * lhs, const robotiq_msgs__msg__GripperStatus * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // object_detection
  if (lhs->object_detection != rhs->object_detection) {
    return false;
  }
  // motor_current
  if (lhs->motor_current != rhs->motor_current) {
    return false;
  }
  // gripper_fault
  if (lhs->gripper_fault != rhs->gripper_fault) {
    return false;
  }
  // gripper_fault_severity
  if (lhs->gripper_fault_severity != rhs->gripper_fault_severity) {
    return false;
  }
  return true;
}

bool
robotiq_msgs__msg__GripperStatus__copy(
  const robotiq_msgs__msg__GripperStatus * input,
  robotiq_msgs__msg__GripperStatus * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // object_detection
  output->object_detection = input->object_detection;
  // motor_current
  output->motor_current = input->motor_current;
  // gripper_fault
  output->gripper_fault = input->gripper_fault;
  // gripper_fault_severity
  output->gripper_fault_severity = input->gripper_fault_severity;
  return true;
}

robotiq_msgs__msg__GripperStatus *
robotiq_msgs__msg__GripperStatus__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotiq_msgs__msg__GripperStatus * msg = (robotiq_msgs__msg__GripperStatus *)allocator.allocate(sizeof(robotiq_msgs__msg__GripperStatus), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robotiq_msgs__msg__GripperStatus));
  bool success = robotiq_msgs__msg__GripperStatus__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robotiq_msgs__msg__GripperStatus__destroy(robotiq_msgs__msg__GripperStatus * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robotiq_msgs__msg__GripperStatus__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robotiq_msgs__msg__GripperStatus__Sequence__init(robotiq_msgs__msg__GripperStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotiq_msgs__msg__GripperStatus * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(robotiq_msgs__msg__GripperStatus)) {
      return false;
    }
    data = (robotiq_msgs__msg__GripperStatus *)allocator.zero_allocate(size, sizeof(robotiq_msgs__msg__GripperStatus), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robotiq_msgs__msg__GripperStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robotiq_msgs__msg__GripperStatus__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
robotiq_msgs__msg__GripperStatus__Sequence__fini(robotiq_msgs__msg__GripperStatus__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      robotiq_msgs__msg__GripperStatus__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

robotiq_msgs__msg__GripperStatus__Sequence *
robotiq_msgs__msg__GripperStatus__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotiq_msgs__msg__GripperStatus__Sequence * array = (robotiq_msgs__msg__GripperStatus__Sequence *)allocator.allocate(sizeof(robotiq_msgs__msg__GripperStatus__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robotiq_msgs__msg__GripperStatus__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robotiq_msgs__msg__GripperStatus__Sequence__destroy(robotiq_msgs__msg__GripperStatus__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robotiq_msgs__msg__GripperStatus__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robotiq_msgs__msg__GripperStatus__Sequence__are_equal(const robotiq_msgs__msg__GripperStatus__Sequence * lhs, const robotiq_msgs__msg__GripperStatus__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robotiq_msgs__msg__GripperStatus__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robotiq_msgs__msg__GripperStatus__Sequence__copy(
  const robotiq_msgs__msg__GripperStatus__Sequence * input,
  robotiq_msgs__msg__GripperStatus__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(robotiq_msgs__msg__GripperStatus)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(robotiq_msgs__msg__GripperStatus);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    robotiq_msgs__msg__GripperStatus * data =
      (robotiq_msgs__msg__GripperStatus *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robotiq_msgs__msg__GripperStatus__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          robotiq_msgs__msg__GripperStatus__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robotiq_msgs__msg__GripperStatus__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
