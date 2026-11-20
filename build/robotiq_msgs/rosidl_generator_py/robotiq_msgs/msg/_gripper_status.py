# generated from rosidl_generator_py/resource/_idl.py.em
# with input from robotiq_msgs:msg/GripperStatus.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GripperStatus(type):
    """Metaclass of message 'GripperStatus'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'MOVING': 0,
        'DETECTED_WHILE_OPENING': 1,
        'DETECTED_WHILE_CLOSING': 2,
        'AT_REQUESTED_POSITION': 3,
        'GRIPPER_FAULT_UNKNOWN': 255,
        'GRIPPER_FAULT_NONE': 0,
        'GRIPPER_FAULT_ACTION_DELAYED': 5,
        'GRIPPER_FAULT_ACTIVATION_REQUIRED': 7,
        'GRIPPER_FAULT_OVER_TEMPERATURE': 8,
        'GRIPPER_FAULT_NO_COMMUNICATION': 9,
        'GRIPPER_FAULT_UNDER_VOLTAGE': 10,
        'GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS': 11,
        'GRIPPER_FAULT_INTERNAL_FAULT': 12,
        'GRIPPER_FAULT_ACTIVATION_FAULT': 13,
        'GRIPPER_FAULT_OVERCURRENT': 14,
        'GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE': 15,
        'GRIPPER_FAULT_SEVERITY_UNKNOWN': 255,
        'GRIPPER_FAULT_SEVERITY_NONE': 0,
        'GRIPPER_FAULT_SEVERITY_WARNING': 1,
        'GRIPPER_FAULT_SEVERITY_MINOR': 2,
        'GRIPPER_FAULT_SEVERITY_MAJOR': 3,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('robotiq_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'robotiq_msgs.msg.GripperStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__gripper_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__gripper_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__gripper_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__gripper_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__gripper_status

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'MOVING': cls.__constants['MOVING'],
            'DETECTED_WHILE_OPENING': cls.__constants['DETECTED_WHILE_OPENING'],
            'DETECTED_WHILE_CLOSING': cls.__constants['DETECTED_WHILE_CLOSING'],
            'AT_REQUESTED_POSITION': cls.__constants['AT_REQUESTED_POSITION'],
            'GRIPPER_FAULT_UNKNOWN': cls.__constants['GRIPPER_FAULT_UNKNOWN'],
            'GRIPPER_FAULT_NONE': cls.__constants['GRIPPER_FAULT_NONE'],
            'GRIPPER_FAULT_ACTION_DELAYED': cls.__constants['GRIPPER_FAULT_ACTION_DELAYED'],
            'GRIPPER_FAULT_ACTIVATION_REQUIRED': cls.__constants['GRIPPER_FAULT_ACTIVATION_REQUIRED'],
            'GRIPPER_FAULT_OVER_TEMPERATURE': cls.__constants['GRIPPER_FAULT_OVER_TEMPERATURE'],
            'GRIPPER_FAULT_NO_COMMUNICATION': cls.__constants['GRIPPER_FAULT_NO_COMMUNICATION'],
            'GRIPPER_FAULT_UNDER_VOLTAGE': cls.__constants['GRIPPER_FAULT_UNDER_VOLTAGE'],
            'GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS': cls.__constants['GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS'],
            'GRIPPER_FAULT_INTERNAL_FAULT': cls.__constants['GRIPPER_FAULT_INTERNAL_FAULT'],
            'GRIPPER_FAULT_ACTIVATION_FAULT': cls.__constants['GRIPPER_FAULT_ACTIVATION_FAULT'],
            'GRIPPER_FAULT_OVERCURRENT': cls.__constants['GRIPPER_FAULT_OVERCURRENT'],
            'GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE': cls.__constants['GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE'],
            'GRIPPER_FAULT_SEVERITY_UNKNOWN': cls.__constants['GRIPPER_FAULT_SEVERITY_UNKNOWN'],
            'GRIPPER_FAULT_SEVERITY_NONE': cls.__constants['GRIPPER_FAULT_SEVERITY_NONE'],
            'GRIPPER_FAULT_SEVERITY_WARNING': cls.__constants['GRIPPER_FAULT_SEVERITY_WARNING'],
            'GRIPPER_FAULT_SEVERITY_MINOR': cls.__constants['GRIPPER_FAULT_SEVERITY_MINOR'],
            'GRIPPER_FAULT_SEVERITY_MAJOR': cls.__constants['GRIPPER_FAULT_SEVERITY_MAJOR'],
            'GRIPPER_FAULT__DEFAULT': 255,
            'GRIPPER_FAULT_SEVERITY__DEFAULT': 255,
        }

    @property
    def MOVING(self):
        """Message constant 'MOVING'."""
        return Metaclass_GripperStatus.__constants['MOVING']

    @property
    def DETECTED_WHILE_OPENING(self):
        """Message constant 'DETECTED_WHILE_OPENING'."""
        return Metaclass_GripperStatus.__constants['DETECTED_WHILE_OPENING']

    @property
    def DETECTED_WHILE_CLOSING(self):
        """Message constant 'DETECTED_WHILE_CLOSING'."""
        return Metaclass_GripperStatus.__constants['DETECTED_WHILE_CLOSING']

    @property
    def AT_REQUESTED_POSITION(self):
        """Message constant 'AT_REQUESTED_POSITION'."""
        return Metaclass_GripperStatus.__constants['AT_REQUESTED_POSITION']

    @property
    def GRIPPER_FAULT_UNKNOWN(self):
        """Message constant 'GRIPPER_FAULT_UNKNOWN'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_UNKNOWN']

    @property
    def GRIPPER_FAULT_NONE(self):
        """Message constant 'GRIPPER_FAULT_NONE'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_NONE']

    @property
    def GRIPPER_FAULT_ACTION_DELAYED(self):
        """Message constant 'GRIPPER_FAULT_ACTION_DELAYED'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_ACTION_DELAYED']

    @property
    def GRIPPER_FAULT_ACTIVATION_REQUIRED(self):
        """Message constant 'GRIPPER_FAULT_ACTIVATION_REQUIRED'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_ACTIVATION_REQUIRED']

    @property
    def GRIPPER_FAULT_OVER_TEMPERATURE(self):
        """Message constant 'GRIPPER_FAULT_OVER_TEMPERATURE'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_OVER_TEMPERATURE']

    @property
    def GRIPPER_FAULT_NO_COMMUNICATION(self):
        """Message constant 'GRIPPER_FAULT_NO_COMMUNICATION'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_NO_COMMUNICATION']

    @property
    def GRIPPER_FAULT_UNDER_VOLTAGE(self):
        """Message constant 'GRIPPER_FAULT_UNDER_VOLTAGE'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_UNDER_VOLTAGE']

    @property
    def GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS(self):
        """Message constant 'GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS']

    @property
    def GRIPPER_FAULT_INTERNAL_FAULT(self):
        """Message constant 'GRIPPER_FAULT_INTERNAL_FAULT'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_INTERNAL_FAULT']

    @property
    def GRIPPER_FAULT_ACTIVATION_FAULT(self):
        """Message constant 'GRIPPER_FAULT_ACTIVATION_FAULT'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_ACTIVATION_FAULT']

    @property
    def GRIPPER_FAULT_OVERCURRENT(self):
        """Message constant 'GRIPPER_FAULT_OVERCURRENT'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_OVERCURRENT']

    @property
    def GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE(self):
        """Message constant 'GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE']

    @property
    def GRIPPER_FAULT_SEVERITY_UNKNOWN(self):
        """Message constant 'GRIPPER_FAULT_SEVERITY_UNKNOWN'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_SEVERITY_UNKNOWN']

    @property
    def GRIPPER_FAULT_SEVERITY_NONE(self):
        """Message constant 'GRIPPER_FAULT_SEVERITY_NONE'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_SEVERITY_NONE']

    @property
    def GRIPPER_FAULT_SEVERITY_WARNING(self):
        """Message constant 'GRIPPER_FAULT_SEVERITY_WARNING'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_SEVERITY_WARNING']

    @property
    def GRIPPER_FAULT_SEVERITY_MINOR(self):
        """Message constant 'GRIPPER_FAULT_SEVERITY_MINOR'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_SEVERITY_MINOR']

    @property
    def GRIPPER_FAULT_SEVERITY_MAJOR(self):
        """Message constant 'GRIPPER_FAULT_SEVERITY_MAJOR'."""
        return Metaclass_GripperStatus.__constants['GRIPPER_FAULT_SEVERITY_MAJOR']

    @property
    def GRIPPER_FAULT__DEFAULT(cls):
        """Return default value for message field 'gripper_fault'."""
        return 255

    @property
    def GRIPPER_FAULT_SEVERITY__DEFAULT(cls):
        """Return default value for message field 'gripper_fault_severity'."""
        return 255


class GripperStatus(metaclass=Metaclass_GripperStatus):
    """
    Message class 'GripperStatus'.

    Constants:
      MOVING
      DETECTED_WHILE_OPENING
      DETECTED_WHILE_CLOSING
      AT_REQUESTED_POSITION
      GRIPPER_FAULT_UNKNOWN
      GRIPPER_FAULT_NONE
      GRIPPER_FAULT_ACTION_DELAYED
      GRIPPER_FAULT_ACTIVATION_REQUIRED
      GRIPPER_FAULT_OVER_TEMPERATURE
      GRIPPER_FAULT_NO_COMMUNICATION
      GRIPPER_FAULT_UNDER_VOLTAGE
      GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS
      GRIPPER_FAULT_INTERNAL_FAULT
      GRIPPER_FAULT_ACTIVATION_FAULT
      GRIPPER_FAULT_OVERCURRENT
      GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE
      GRIPPER_FAULT_SEVERITY_UNKNOWN
      GRIPPER_FAULT_SEVERITY_NONE
      GRIPPER_FAULT_SEVERITY_WARNING
      GRIPPER_FAULT_SEVERITY_MINOR
      GRIPPER_FAULT_SEVERITY_MAJOR
    """

    __slots__ = [
        '_header',
        '_object_detection',
        '_motor_current',
        '_gripper_fault',
        '_gripper_fault_severity',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'object_detection': 'uint8',
        'motor_current': 'double',
        'gripper_fault': 'uint8',
        'gripper_fault_severity': 'uint8',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.object_detection = kwargs.get('object_detection', int())
        self.motor_current = kwargs.get('motor_current', float())
        self.gripper_fault = kwargs.get(
            'gripper_fault', GripperStatus.GRIPPER_FAULT__DEFAULT)
        self.gripper_fault_severity = kwargs.get(
            'gripper_fault_severity', GripperStatus.GRIPPER_FAULT_SEVERITY__DEFAULT)

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.object_detection != other.object_detection:
            return False
        if self.motor_current != other.motor_current:
            return False
        if self.gripper_fault != other.gripper_fault:
            return False
        if self.gripper_fault_severity != other.gripper_fault_severity:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if self._check_fields:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def object_detection(self):
        """Message field 'object_detection'."""
        return self._object_detection

    @object_detection.setter
    def object_detection(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'object_detection' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'object_detection' field must be an unsigned integer in [0, 255]"
        self._object_detection = value

    @builtins.property
    def motor_current(self):
        """Message field 'motor_current'."""
        return self._motor_current

    @motor_current.setter
    def motor_current(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'motor_current' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'motor_current' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._motor_current = value

    @builtins.property
    def gripper_fault(self):
        """Message field 'gripper_fault'."""
        return self._gripper_fault

    @gripper_fault.setter
    def gripper_fault(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'gripper_fault' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'gripper_fault' field must be an unsigned integer in [0, 255]"
        self._gripper_fault = value

    @builtins.property
    def gripper_fault_severity(self):
        """Message field 'gripper_fault_severity'."""
        return self._gripper_fault_severity

    @gripper_fault_severity.setter
    def gripper_fault_severity(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'gripper_fault_severity' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'gripper_fault_severity' field must be an unsigned integer in [0, 255]"
        self._gripper_fault_severity = value
