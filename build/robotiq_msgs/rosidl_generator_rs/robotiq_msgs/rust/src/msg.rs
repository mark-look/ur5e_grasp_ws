#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to robotiq_msgs__msg__GripperStatus
/// What the gripper reports about itself, decoded. The driver reads these out of
/// the status block every exchange cycle; a broadcaster republishes them here so
/// that a client off the controller manager can read them without re-deriving
/// anything from a register.

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GripperStatus {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::GripperStatus::default())
  }
}

impl rosidl_runtime_rs::Message for GripperStatus {
  type RmwMsg = super::msg::rmw::GripperStatus;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        object_detection: msg.object_detection,
        motor_current: msg.motor_current,
        gripper_fault: msg.gripper_fault,
        gripper_fault_severity: msg.gripper_fault_severity,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      object_detection: msg.object_detection,
      motor_current: msg.motor_current,
      gripper_fault: msg.gripper_fault,
      gripper_fault_severity: msg.gripper_fault_severity,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      object_detection: msg.object_detection,
      motor_current: msg.motor_current,
      gripper_fault: msg.gripper_fault,
      gripper_fault_severity: msg.gripper_fault_severity,
    }
  }
}


