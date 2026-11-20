#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "robotiq_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__robotiq_msgs__msg__GripperStatus() -> *const std::ffi::c_void;
}

#[link(name = "robotiq_msgs__rosidl_generator_c")]
extern "C" {
    fn robotiq_msgs__msg__GripperStatus__init(msg: *mut GripperStatus) -> bool;
    fn robotiq_msgs__msg__GripperStatus__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GripperStatus>, size: usize) -> bool;
    fn robotiq_msgs__msg__GripperStatus__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GripperStatus>);
    fn robotiq_msgs__msg__GripperStatus__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GripperStatus>, out_seq: *mut rosidl_runtime_rs::Sequence<GripperStatus>) -> bool;
}

// Corresponds to robotiq_msgs__msg__GripperStatus
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// What the gripper reports about itself, decoded. The driver reads these out of
/// the status block every exchange cycle; a broadcaster republishes them here so
/// that a client off the controller manager can read them without re-deriving
/// anything from a register.

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GripperStatus {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub object_detection: u8,

    /// gCU in amperes. Motor current, not grip force, and not convertible to one.
    pub motor_current: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub gripper_fault: u8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub gripper_fault_severity: u8,

}

impl GripperStatus {
    /// gOBJ. The gripper's own answer to "am I holding something", and the only
    /// authoritative one: a stall flag or a position comparison is a guess at this.
    pub const MOVING: u8 = 0;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const DETECTED_WHILE_OPENING: u8 = 1;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const DETECTED_WHILE_CLOSING: u8 = 2;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const AT_REQUESTED_POSITION: u8 = 3;

    /// gFLT, as the instruction manual numbers it. The register is four bits wide, so
    /// a code the manual does not list can still arrive: treat it as an undefined
    /// fault, which gripper_fault_severity reports as major.
    ///
    /// UNKNOWN is outside the register, and says the gripper did not report a fault
    /// this cycle, either because the hardware exports no fault interface or because
    /// the reading failed. It is not NONE: an unfaulted gripper and a gripper that
    /// is not reporting a fault state are different, and only one of them is safe to act on.
    pub const GRIPPER_FAULT_UNKNOWN: u8 = 255;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_NONE: u8 = 0;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_ACTION_DELAYED: u8 = 5;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_ACTIVATION_REQUIRED: u8 = 7;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_OVER_TEMPERATURE: u8 = 8;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_NO_COMMUNICATION: u8 = 9;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_UNDER_VOLTAGE: u8 = 10;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_AUTOMATIC_RELEASE_IN_PROGRESS: u8 = 11;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_INTERNAL_FAULT: u8 = 12;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_ACTIVATION_FAULT: u8 = 13;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_OVERCURRENT: u8 = 14;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_AUTOMATIC_RELEASE_COMPLETE: u8 = 15;

    /// How bad the gripper fault is. A major fault clears only on a reactivation;
    /// the manual calls the warning tier "priority faults". UNKNOWN accompanies
    /// GRIPPER_FAULT_UNKNOWN: the two fields are exported together or not at all.
    pub const GRIPPER_FAULT_SEVERITY_UNKNOWN: u8 = 255;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_SEVERITY_NONE: u8 = 0;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_SEVERITY_WARNING: u8 = 1;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_SEVERITY_MINOR: u8 = 2;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const GRIPPER_FAULT_SEVERITY_MAJOR: u8 = 3;

}


impl Default for GripperStatus {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !robotiq_msgs__msg__GripperStatus__init(&mut msg as *mut _) {
        panic!("Call to robotiq_msgs__msg__GripperStatus__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GripperStatus {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotiq_msgs__msg__GripperStatus__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotiq_msgs__msg__GripperStatus__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotiq_msgs__msg__GripperStatus__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GripperStatus {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GripperStatus where Self: Sized {
  const TYPE_NAME: &'static str = "robotiq_msgs/msg/GripperStatus";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__robotiq_msgs__msg__GripperStatus() }
  }
}


