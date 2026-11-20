// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from robotiq_msgs:msg/GripperStatus.idl
// generated code does not contain a copyright notice

#include "robotiq_msgs/msg/detail/gripper_status__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_robotiq_msgs
const rosidl_type_hash_t *
robotiq_msgs__msg__GripperStatus__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xa7, 0x65, 0x51, 0x26, 0xab, 0x92, 0xbc, 0x29,
      0x1e, 0x4e, 0x6e, 0x6e, 0x90, 0x15, 0x98, 0x92,
      0x91, 0x0a, 0x3b, 0x06, 0x98, 0xe5, 0x19, 0x97,
      0xbf, 0x9d, 0x4b, 0xff, 0x7b, 0x25, 0x09, 0xe2,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "std_msgs/msg/detail/header__functions.h"
#include "builtin_interfaces/msg/detail/time__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t std_msgs__msg__Header__EXPECTED_HASH = {1, {
    0xf4, 0x9f, 0xb3, 0xae, 0x2c, 0xf0, 0x70, 0xf7,
    0x93, 0x64, 0x5f, 0xf7, 0x49, 0x68, 0x3a, 0xc6,
    0xb0, 0x62, 0x03, 0xe4, 0x1c, 0x89, 0x1e, 0x17,
    0x70, 0x1b, 0x1c, 0xb5, 0x97, 0xce, 0x6a, 0x01,
  }};
#endif

static char robotiq_msgs__msg__GripperStatus__TYPE_NAME[] = "robotiq_msgs/msg/GripperStatus";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char std_msgs__msg__Header__TYPE_NAME[] = "std_msgs/msg/Header";

// Define type names, field names, and default values
static char robotiq_msgs__msg__GripperStatus__FIELD_NAME__header[] = "header";
static char robotiq_msgs__msg__GripperStatus__FIELD_NAME__object_detection[] = "object_detection";
static char robotiq_msgs__msg__GripperStatus__FIELD_NAME__motor_current[] = "motor_current";
static char robotiq_msgs__msg__GripperStatus__FIELD_NAME__gripper_fault[] = "gripper_fault";
static char robotiq_msgs__msg__GripperStatus__DEFAULT_VALUE__gripper_fault[] = "255";
static char robotiq_msgs__msg__GripperStatus__FIELD_NAME__gripper_fault_severity[] = "gripper_fault_severity";
static char robotiq_msgs__msg__GripperStatus__DEFAULT_VALUE__gripper_fault_severity[] = "255";

static rosidl_runtime_c__type_description__Field robotiq_msgs__msg__GripperStatus__FIELDS[] = {
  {
    {robotiq_msgs__msg__GripperStatus__FIELD_NAME__header, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    },
    {NULL, 0, 0},
  },
  {
    {robotiq_msgs__msg__GripperStatus__FIELD_NAME__object_detection, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {robotiq_msgs__msg__GripperStatus__FIELD_NAME__motor_current, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {robotiq_msgs__msg__GripperStatus__FIELD_NAME__gripper_fault, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {robotiq_msgs__msg__GripperStatus__DEFAULT_VALUE__gripper_fault, 3, 3},
  },
  {
    {robotiq_msgs__msg__GripperStatus__FIELD_NAME__gripper_fault_severity, 22, 22},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {robotiq_msgs__msg__GripperStatus__DEFAULT_VALUE__gripper_fault_severity, 3, 3},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription robotiq_msgs__msg__GripperStatus__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robotiq_msgs__msg__GripperStatus__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robotiq_msgs__msg__GripperStatus__TYPE_NAME, 30, 30},
      {robotiq_msgs__msg__GripperStatus__FIELDS, 5, 5},
    },
    {robotiq_msgs__msg__GripperStatus__REFERENCED_TYPE_DESCRIPTIONS, 2, 2},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__Header__EXPECTED_HASH, std_msgs__msg__Header__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = std_msgs__msg__Header__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# What the gripper reports about itself, decoded. The driver reads these out of\n"
  "# the status block every exchange cycle; a broadcaster republishes them here so\n"
  "# that a client off the controller manager can read them without re-deriving\n"
  "# anything from a register.\n"
  "\n"
  "std_msgs/Header header\n"
  "\n"
  "# gOBJ. The gripper\\'s own answer to \"am I holding something\", and the only\n"
  "# authoritative one: a stall flag or a position comparison is a guess at this.\n"
  "uint8 MOVING=0\n"
  "uint8 DETECTED_WHILE_OPENING=1\n"
  "uint8 DETECTED_WHILE_CLOSING=2\n"
  "uint8 AT_REQUESTED_POSITION=3\n"
  "uint8 object_detection\n"
  "\n"
  "# gCU in amperes. Motor current, not grip force, and not convertible to one.\n"
  "float64 motor_current\n"
  "\n"
  "# gFLT, as the instruction manual numbers it. The register is four bits wide, so\n"
  "# a code the manual does not list can still arrive: treat it as an undefined\n"
  "# fault, which gripper_fault_severity reports as major.\n"
  "#\n"
  "# UNKNOWN is outside the register, and says the gripper did not report a fault\n"
  "# this cycle, either because the hardware exports no fault interface or because\n"
  "# the reading failed. It is not NONE: an unfaulted gripper and a gripper that\n"
  "# is not reporting a fault state are different, and only one of them is safe to act on.\n"
  "uint8 GRIPPER_FAULT_UNKNOWN=255\n"
  "uint8 GRIPPER_FAULT_NONE=0\n"
  "uint8 GRIPPER_FAULT_ACTION_DELAYED=5\n"
  "uint8 GRIPPER_FAULT_ACTIVATION_REQUIRED=7\n"
  "uint8 GRIPPER_FAULT_OVER_TEMPERATURE=8\n"
  "uint8 GRIPPER_FAULT_NO_COMMUNICATION=9\n"
  "uint8 GRIPPER_FAULT_UNDER_VOLTAGE=10\n"
  "uint8 GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS=11\n"
  "uint8 GRIPPER_FAULT_INTERNAL_FAULT=12\n"
  "uint8 GRIPPER_FAULT_ACTIVATION_FAULT=13\n"
  "uint8 GRIPPER_FAULT_OVERCURRENT=14\n"
  "uint8 GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE=15\n"
  "uint8 gripper_fault 255\n"
  "\n"
  "# How bad the gripper fault is. A major fault clears only on a reactivation;\n"
  "# the manual calls the warning tier \"priority faults\". UNKNOWN accompanies\n"
  "# GRIPPER_FAULT_UNKNOWN: the two fields are exported together or not at all.\n"
  "uint8 GRIPPER_FAULT_SEVERITY_UNKNOWN=255\n"
  "uint8 GRIPPER_FAULT_SEVERITY_NONE=0\n"
  "uint8 GRIPPER_FAULT_SEVERITY_WARNING=1\n"
  "uint8 GRIPPER_FAULT_SEVERITY_MINOR=2\n"
  "uint8 GRIPPER_FAULT_SEVERITY_MAJOR=3\n"
  "uint8 gripper_fault_severity 255";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
robotiq_msgs__msg__GripperStatus__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robotiq_msgs__msg__GripperStatus__TYPE_NAME, 30, 30},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 2162, 2162},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robotiq_msgs__msg__GripperStatus__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[3];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 3, 3};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robotiq_msgs__msg__GripperStatus__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *std_msgs__msg__Header__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
