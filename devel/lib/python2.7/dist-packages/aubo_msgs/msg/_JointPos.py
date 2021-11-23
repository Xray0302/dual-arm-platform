# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from aubo_msgs/JointPos.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class JointPos(genpy.Message):
  _md5sum = "b0068422b386ec8608fa05052ffe139f"
  _type = "aubo_msgs/JointPos"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32 joint1
float32 joint2
float32 joint3
float32 joint4
float32 joint5
float32 joint6
"""
  __slots__ = ['joint1','joint2','joint3','joint4','joint5','joint6']
  _slot_types = ['float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       joint1,joint2,joint3,joint4,joint5,joint6

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(JointPos, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.joint1 is None:
        self.joint1 = 0.
      if self.joint2 is None:
        self.joint2 = 0.
      if self.joint3 is None:
        self.joint3 = 0.
      if self.joint4 is None:
        self.joint4 = 0.
      if self.joint5 is None:
        self.joint5 = 0.
      if self.joint6 is None:
        self.joint6 = 0.
    else:
      self.joint1 = 0.
      self.joint2 = 0.
      self.joint3 = 0.
      self.joint4 = 0.
      self.joint5 = 0.
      self.joint6 = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_6f().pack(_x.joint1, _x.joint2, _x.joint3, _x.joint4, _x.joint5, _x.joint6))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.joint1, _x.joint2, _x.joint3, _x.joint4, _x.joint5, _x.joint6,) = _get_struct_6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_6f().pack(_x.joint1, _x.joint2, _x.joint3, _x.joint4, _x.joint5, _x.joint6))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.joint1, _x.joint2, _x.joint3, _x.joint4, _x.joint5, _x.joint6,) = _get_struct_6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6f = None
def _get_struct_6f():
    global _struct_6f
    if _struct_6f is None:
        _struct_6f = struct.Struct("<6f")
    return _struct_6f
