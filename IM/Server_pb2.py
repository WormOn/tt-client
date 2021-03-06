# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IM.Server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import IM.BaseDefine_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='IM.Server.proto',
  package='IM.Server',
  serialized_pb=_b('\n\x0fIM.Server.proto\x12\tIM.Server\x1a\x13IM.BaseDefine.proto\"%\n\x13IMStopReceivePacket\x12\x0e\n\x06result\x18\x01 \x02(\r\"I\n\rIMValidateReq\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\x8f\x01\n\rIMValidateRsp\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12\x13\n\x0bresult_code\x18\x02 \x02(\r\x12\x15\n\rresult_string\x18\x03 \x01(\t\x12*\n\tuser_info\x18\x04 \x01(\x0b\x32\x17.IM.BaseDefine.UserInfo\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\";\n\x13IMGetDeviceTokenReq\x12\x0f\n\x07user_id\x18\x01 \x03(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"a\n\x13IMGetDeviceTokenRsp\x12\x35\n\x0fuser_token_info\x18\x01 \x03(\x0b\x32\x1c.IM.BaseDefine.UserTokenInfo\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\x1b\n\tIMRoleSet\x12\x0e\n\x06master\x18\x01 \x02(\r\"I\n\x10IMOnlineUserInfo\x12\x35\n\x0euser_stat_list\x18\x01 \x03(\x0b\x32\x1d.IM.BaseDefine.ServerUserStat\"v\n\rIMMsgServInfo\x12\x0b\n\x03ip1\x18\x01 \x02(\t\x12\x0b\n\x03ip2\x18\x02 \x02(\t\x12\x0c\n\x04port\x18\x03 \x02(\r\x12\x14\n\x0cmax_conn_cnt\x18\x04 \x02(\r\x12\x14\n\x0c\x63ur_conn_cnt\x18\x05 \x02(\r\x12\x11\n\thost_name\x18\x06 \x02(\t\"j\n\x12IMUserStatusUpdate\x12\x13\n\x0buser_status\x18\x01 \x02(\r\x12\x0f\n\x07user_id\x18\x02 \x02(\r\x12.\n\x0b\x63lient_type\x18\x03 \x02(\x0e\x32\x19.IM.BaseDefine.ClientType\"7\n\x0fIMUserCntUpdate\x12\x13\n\x0buser_action\x18\x01 \x02(\r\x12\x0f\n\x07user_id\x18\x02 \x02(\r\"c\n\x10IMServerKickUser\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12.\n\x0b\x63lient_type\x18\x02 \x02(\x0e\x32\x19.IM.BaseDefine.ClientType\x12\x0e\n\x06reason\x18\x03 \x02(\r\"D\n\x1bIMServerPCLoginStatusNotify\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x14\n\x0clogin_status\x18\x02 \x02(\r\"e\n\x0fIMPushToUserReq\x12\r\n\x05\x66lash\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\t\x12\x35\n\x0fuser_token_list\x18\x03 \x03(\x0b\x32\x1c.IM.BaseDefine.UserTokenInfo\"F\n\x0fIMPushToUserRsp\x12\x33\n\x10push_result_list\x18\x01 \x03(\x0b\x32\x19.IM.BaseDefine.PushResult\"M\n\x13IMGroupGetShieldReq\x12\x10\n\x08group_id\x18\x01 \x02(\r\x12\x0f\n\x07user_id\x18\x02 \x03(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"u\n\x13IMGroupGetShieldRsp\x12\x10\n\x08group_id\x18\x01 \x02(\r\x12\x37\n\x12shield_status_list\x18\x02 \x03(\x0b\x32\x1b.IM.BaseDefine.ShieldStatus\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\xad\x01\n\x11IMFileTransferReq\x12\x14\n\x0c\x66rom_user_id\x18\x01 \x02(\r\x12\x12\n\nto_user_id\x18\x02 \x02(\r\x12\x11\n\tfile_name\x18\x03 \x02(\t\x12\x11\n\tfile_size\x18\x04 \x02(\r\x12\x33\n\ntrans_mode\x18\x05 \x02(\x0e\x32\x1f.IM.BaseDefine.TransferFileType\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\xd3\x01\n\x11IMFileTransferRsp\x12\x13\n\x0bresult_code\x18\x01 \x02(\r\x12\x14\n\x0c\x66rom_user_id\x18\x02 \x02(\r\x12\x12\n\nto_user_id\x18\x03 \x02(\r\x12\x11\n\tfile_name\x18\x04 \x01(\t\x12\x11\n\tfile_size\x18\x05 \x01(\r\x12\x0f\n\x07task_id\x18\x06 \x01(\t\x12\x33\n\ntrans_mode\x18\x07 \x01(\x0e\x32\x1f.IM.BaseDefine.TransferFileType\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\x13\n\x11IMFileServerIPReq\"@\n\x11IMFileServerIPRsp\x12+\n\x0cip_addr_list\x18\x01 \x03(\x0b\x32\x15.IM.BaseDefine.IpAddrB\x02H\x03')
  ,
  dependencies=[IM.BaseDefine_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IMSTOPRECEIVEPACKET = _descriptor.Descriptor(
  name='IMStopReceivePacket',
  full_name='IM.Server.IMStopReceivePacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='IM.Server.IMStopReceivePacket.result', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=88,
)


_IMVALIDATEREQ = _descriptor.Descriptor(
  name='IMValidateReq',
  full_name='IM.Server.IMValidateReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='IM.Server.IMValidateReq.user_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='IM.Server.IMValidateReq.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Server.IMValidateReq.attach_data', index=2,
      number=20, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=163,
)


_IMVALIDATERSP = _descriptor.Descriptor(
  name='IMValidateRsp',
  full_name='IM.Server.IMValidateRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='IM.Server.IMValidateRsp.user_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_code', full_name='IM.Server.IMValidateRsp.result_code', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_string', full_name='IM.Server.IMValidateRsp.result_string', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_info', full_name='IM.Server.IMValidateRsp.user_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Server.IMValidateRsp.attach_data', index=4,
      number=20, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=309,
)


_IMGETDEVICETOKENREQ = _descriptor.Descriptor(
  name='IMGetDeviceTokenReq',
  full_name='IM.Server.IMGetDeviceTokenReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Server.IMGetDeviceTokenReq.user_id', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Server.IMGetDeviceTokenReq.attach_data', index=1,
      number=20, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=370,
)


_IMGETDEVICETOKENRSP = _descriptor.Descriptor(
  name='IMGetDeviceTokenRsp',
  full_name='IM.Server.IMGetDeviceTokenRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_token_info', full_name='IM.Server.IMGetDeviceTokenRsp.user_token_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Server.IMGetDeviceTokenRsp.attach_data', index=1,
      number=20, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=469,
)


_IMROLESET = _descriptor.Descriptor(
  name='IMRoleSet',
  full_name='IM.Server.IMRoleSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='master', full_name='IM.Server.IMRoleSet.master', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=471,
  serialized_end=498,
)


_IMONLINEUSERINFO = _descriptor.Descriptor(
  name='IMOnlineUserInfo',
  full_name='IM.Server.IMOnlineUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_stat_list', full_name='IM.Server.IMOnlineUserInfo.user_stat_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=500,
  serialized_end=573,
)


_IMMSGSERVINFO = _descriptor.Descriptor(
  name='IMMsgServInfo',
  full_name='IM.Server.IMMsgServInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip1', full_name='IM.Server.IMMsgServInfo.ip1', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip2', full_name='IM.Server.IMMsgServInfo.ip2', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='IM.Server.IMMsgServInfo.port', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_conn_cnt', full_name='IM.Server.IMMsgServInfo.max_conn_cnt', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cur_conn_cnt', full_name='IM.Server.IMMsgServInfo.cur_conn_cnt', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host_name', full_name='IM.Server.IMMsgServInfo.host_name', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=575,
  serialized_end=693,
)


_IMUSERSTATUSUPDATE = _descriptor.Descriptor(
  name='IMUserStatusUpdate',
  full_name='IM.Server.IMUserStatusUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_status', full_name='IM.Server.IMUserStatusUpdate.user_status', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Server.IMUserStatusUpdate.user_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_type', full_name='IM.Server.IMUserStatusUpdate.client_type', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=695,
  serialized_end=801,
)


_IMUSERCNTUPDATE = _descriptor.Descriptor(
  name='IMUserCntUpdate',
  full_name='IM.Server.IMUserCntUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_action', full_name='IM.Server.IMUserCntUpdate.user_action', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Server.IMUserCntUpdate.user_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=803,
  serialized_end=858,
)


_IMSERVERKICKUSER = _descriptor.Descriptor(
  name='IMServerKickUser',
  full_name='IM.Server.IMServerKickUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Server.IMServerKickUser.user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_type', full_name='IM.Server.IMServerKickUser.client_type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='IM.Server.IMServerKickUser.reason', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=860,
  serialized_end=959,
)


_IMSERVERPCLOGINSTATUSNOTIFY = _descriptor.Descriptor(
  name='IMServerPCLoginStatusNotify',
  full_name='IM.Server.IMServerPCLoginStatusNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Server.IMServerPCLoginStatusNotify.user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login_status', full_name='IM.Server.IMServerPCLoginStatusNotify.login_status', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=961,
  serialized_end=1029,
)


_IMPUSHTOUSERREQ = _descriptor.Descriptor(
  name='IMPushToUserReq',
  full_name='IM.Server.IMPushToUserReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flash', full_name='IM.Server.IMPushToUserReq.flash', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='IM.Server.IMPushToUserReq.data', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_token_list', full_name='IM.Server.IMPushToUserReq.user_token_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1031,
  serialized_end=1132,
)


_IMPUSHTOUSERRSP = _descriptor.Descriptor(
  name='IMPushToUserRsp',
  full_name='IM.Server.IMPushToUserRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='push_result_list', full_name='IM.Server.IMPushToUserRsp.push_result_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1134,
  serialized_end=1204,
)


_IMGROUPGETSHIELDREQ = _descriptor.Descriptor(
  name='IMGroupGetShieldReq',
  full_name='IM.Server.IMGroupGetShieldReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='IM.Server.IMGroupGetShieldReq.group_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Server.IMGroupGetShieldReq.user_id', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Server.IMGroupGetShieldReq.attach_data', index=2,
      number=20, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1206,
  serialized_end=1283,
)


_IMGROUPGETSHIELDRSP = _descriptor.Descriptor(
  name='IMGroupGetShieldRsp',
  full_name='IM.Server.IMGroupGetShieldRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='IM.Server.IMGroupGetShieldRsp.group_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shield_status_list', full_name='IM.Server.IMGroupGetShieldRsp.shield_status_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Server.IMGroupGetShieldRsp.attach_data', index=2,
      number=20, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1285,
  serialized_end=1402,
)


_IMFILETRANSFERREQ = _descriptor.Descriptor(
  name='IMFileTransferReq',
  full_name='IM.Server.IMFileTransferReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_user_id', full_name='IM.Server.IMFileTransferReq.from_user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_user_id', full_name='IM.Server.IMFileTransferReq.to_user_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='IM.Server.IMFileTransferReq.file_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='IM.Server.IMFileTransferReq.file_size', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trans_mode', full_name='IM.Server.IMFileTransferReq.trans_mode', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Server.IMFileTransferReq.attach_data', index=5,
      number=20, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1405,
  serialized_end=1578,
)


_IMFILETRANSFERRSP = _descriptor.Descriptor(
  name='IMFileTransferRsp',
  full_name='IM.Server.IMFileTransferRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_code', full_name='IM.Server.IMFileTransferRsp.result_code', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_user_id', full_name='IM.Server.IMFileTransferRsp.from_user_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_user_id', full_name='IM.Server.IMFileTransferRsp.to_user_id', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='IM.Server.IMFileTransferRsp.file_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='IM.Server.IMFileTransferRsp.file_size', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='IM.Server.IMFileTransferRsp.task_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trans_mode', full_name='IM.Server.IMFileTransferRsp.trans_mode', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Server.IMFileTransferRsp.attach_data', index=7,
      number=20, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1581,
  serialized_end=1792,
)


_IMFILESERVERIPREQ = _descriptor.Descriptor(
  name='IMFileServerIPReq',
  full_name='IM.Server.IMFileServerIPReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1794,
  serialized_end=1813,
)


_IMFILESERVERIPRSP = _descriptor.Descriptor(
  name='IMFileServerIPRsp',
  full_name='IM.Server.IMFileServerIPRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_addr_list', full_name='IM.Server.IMFileServerIPRsp.ip_addr_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1815,
  serialized_end=1879,
)

_IMVALIDATERSP.fields_by_name['user_info'].message_type = IM.BaseDefine_pb2._USERINFO
_IMGETDEVICETOKENRSP.fields_by_name['user_token_info'].message_type = IM.BaseDefine_pb2._USERTOKENINFO
_IMONLINEUSERINFO.fields_by_name['user_stat_list'].message_type = IM.BaseDefine_pb2._SERVERUSERSTAT
_IMUSERSTATUSUPDATE.fields_by_name['client_type'].enum_type = IM.BaseDefine_pb2._CLIENTTYPE
_IMSERVERKICKUSER.fields_by_name['client_type'].enum_type = IM.BaseDefine_pb2._CLIENTTYPE
_IMPUSHTOUSERREQ.fields_by_name['user_token_list'].message_type = IM.BaseDefine_pb2._USERTOKENINFO
_IMPUSHTOUSERRSP.fields_by_name['push_result_list'].message_type = IM.BaseDefine_pb2._PUSHRESULT
_IMGROUPGETSHIELDRSP.fields_by_name['shield_status_list'].message_type = IM.BaseDefine_pb2._SHIELDSTATUS
_IMFILETRANSFERREQ.fields_by_name['trans_mode'].enum_type = IM.BaseDefine_pb2._TRANSFERFILETYPE
_IMFILETRANSFERRSP.fields_by_name['trans_mode'].enum_type = IM.BaseDefine_pb2._TRANSFERFILETYPE
_IMFILESERVERIPRSP.fields_by_name['ip_addr_list'].message_type = IM.BaseDefine_pb2._IPADDR
DESCRIPTOR.message_types_by_name['IMStopReceivePacket'] = _IMSTOPRECEIVEPACKET
DESCRIPTOR.message_types_by_name['IMValidateReq'] = _IMVALIDATEREQ
DESCRIPTOR.message_types_by_name['IMValidateRsp'] = _IMVALIDATERSP
DESCRIPTOR.message_types_by_name['IMGetDeviceTokenReq'] = _IMGETDEVICETOKENREQ
DESCRIPTOR.message_types_by_name['IMGetDeviceTokenRsp'] = _IMGETDEVICETOKENRSP
DESCRIPTOR.message_types_by_name['IMRoleSet'] = _IMROLESET
DESCRIPTOR.message_types_by_name['IMOnlineUserInfo'] = _IMONLINEUSERINFO
DESCRIPTOR.message_types_by_name['IMMsgServInfo'] = _IMMSGSERVINFO
DESCRIPTOR.message_types_by_name['IMUserStatusUpdate'] = _IMUSERSTATUSUPDATE
DESCRIPTOR.message_types_by_name['IMUserCntUpdate'] = _IMUSERCNTUPDATE
DESCRIPTOR.message_types_by_name['IMServerKickUser'] = _IMSERVERKICKUSER
DESCRIPTOR.message_types_by_name['IMServerPCLoginStatusNotify'] = _IMSERVERPCLOGINSTATUSNOTIFY
DESCRIPTOR.message_types_by_name['IMPushToUserReq'] = _IMPUSHTOUSERREQ
DESCRIPTOR.message_types_by_name['IMPushToUserRsp'] = _IMPUSHTOUSERRSP
DESCRIPTOR.message_types_by_name['IMGroupGetShieldReq'] = _IMGROUPGETSHIELDREQ
DESCRIPTOR.message_types_by_name['IMGroupGetShieldRsp'] = _IMGROUPGETSHIELDRSP
DESCRIPTOR.message_types_by_name['IMFileTransferReq'] = _IMFILETRANSFERREQ
DESCRIPTOR.message_types_by_name['IMFileTransferRsp'] = _IMFILETRANSFERRSP
DESCRIPTOR.message_types_by_name['IMFileServerIPReq'] = _IMFILESERVERIPREQ
DESCRIPTOR.message_types_by_name['IMFileServerIPRsp'] = _IMFILESERVERIPRSP

IMStopReceivePacket = _reflection.GeneratedProtocolMessageType('IMStopReceivePacket', (_message.Message,), dict(
  DESCRIPTOR = _IMSTOPRECEIVEPACKET,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMStopReceivePacket)
  ))
_sym_db.RegisterMessage(IMStopReceivePacket)

IMValidateReq = _reflection.GeneratedProtocolMessageType('IMValidateReq', (_message.Message,), dict(
  DESCRIPTOR = _IMVALIDATEREQ,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMValidateReq)
  ))
_sym_db.RegisterMessage(IMValidateReq)

IMValidateRsp = _reflection.GeneratedProtocolMessageType('IMValidateRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMVALIDATERSP,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMValidateRsp)
  ))
_sym_db.RegisterMessage(IMValidateRsp)

IMGetDeviceTokenReq = _reflection.GeneratedProtocolMessageType('IMGetDeviceTokenReq', (_message.Message,), dict(
  DESCRIPTOR = _IMGETDEVICETOKENREQ,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMGetDeviceTokenReq)
  ))
_sym_db.RegisterMessage(IMGetDeviceTokenReq)

IMGetDeviceTokenRsp = _reflection.GeneratedProtocolMessageType('IMGetDeviceTokenRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMGETDEVICETOKENRSP,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMGetDeviceTokenRsp)
  ))
_sym_db.RegisterMessage(IMGetDeviceTokenRsp)

IMRoleSet = _reflection.GeneratedProtocolMessageType('IMRoleSet', (_message.Message,), dict(
  DESCRIPTOR = _IMROLESET,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMRoleSet)
  ))
_sym_db.RegisterMessage(IMRoleSet)

IMOnlineUserInfo = _reflection.GeneratedProtocolMessageType('IMOnlineUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _IMONLINEUSERINFO,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMOnlineUserInfo)
  ))
_sym_db.RegisterMessage(IMOnlineUserInfo)

IMMsgServInfo = _reflection.GeneratedProtocolMessageType('IMMsgServInfo', (_message.Message,), dict(
  DESCRIPTOR = _IMMSGSERVINFO,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMMsgServInfo)
  ))
_sym_db.RegisterMessage(IMMsgServInfo)

IMUserStatusUpdate = _reflection.GeneratedProtocolMessageType('IMUserStatusUpdate', (_message.Message,), dict(
  DESCRIPTOR = _IMUSERSTATUSUPDATE,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMUserStatusUpdate)
  ))
_sym_db.RegisterMessage(IMUserStatusUpdate)

IMUserCntUpdate = _reflection.GeneratedProtocolMessageType('IMUserCntUpdate', (_message.Message,), dict(
  DESCRIPTOR = _IMUSERCNTUPDATE,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMUserCntUpdate)
  ))
_sym_db.RegisterMessage(IMUserCntUpdate)

IMServerKickUser = _reflection.GeneratedProtocolMessageType('IMServerKickUser', (_message.Message,), dict(
  DESCRIPTOR = _IMSERVERKICKUSER,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMServerKickUser)
  ))
_sym_db.RegisterMessage(IMServerKickUser)

IMServerPCLoginStatusNotify = _reflection.GeneratedProtocolMessageType('IMServerPCLoginStatusNotify', (_message.Message,), dict(
  DESCRIPTOR = _IMSERVERPCLOGINSTATUSNOTIFY,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMServerPCLoginStatusNotify)
  ))
_sym_db.RegisterMessage(IMServerPCLoginStatusNotify)

IMPushToUserReq = _reflection.GeneratedProtocolMessageType('IMPushToUserReq', (_message.Message,), dict(
  DESCRIPTOR = _IMPUSHTOUSERREQ,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMPushToUserReq)
  ))
_sym_db.RegisterMessage(IMPushToUserReq)

IMPushToUserRsp = _reflection.GeneratedProtocolMessageType('IMPushToUserRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMPUSHTOUSERRSP,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMPushToUserRsp)
  ))
_sym_db.RegisterMessage(IMPushToUserRsp)

IMGroupGetShieldReq = _reflection.GeneratedProtocolMessageType('IMGroupGetShieldReq', (_message.Message,), dict(
  DESCRIPTOR = _IMGROUPGETSHIELDREQ,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMGroupGetShieldReq)
  ))
_sym_db.RegisterMessage(IMGroupGetShieldReq)

IMGroupGetShieldRsp = _reflection.GeneratedProtocolMessageType('IMGroupGetShieldRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMGROUPGETSHIELDRSP,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMGroupGetShieldRsp)
  ))
_sym_db.RegisterMessage(IMGroupGetShieldRsp)

IMFileTransferReq = _reflection.GeneratedProtocolMessageType('IMFileTransferReq', (_message.Message,), dict(
  DESCRIPTOR = _IMFILETRANSFERREQ,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMFileTransferReq)
  ))
_sym_db.RegisterMessage(IMFileTransferReq)

IMFileTransferRsp = _reflection.GeneratedProtocolMessageType('IMFileTransferRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMFILETRANSFERRSP,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMFileTransferRsp)
  ))
_sym_db.RegisterMessage(IMFileTransferRsp)

IMFileServerIPReq = _reflection.GeneratedProtocolMessageType('IMFileServerIPReq', (_message.Message,), dict(
  DESCRIPTOR = _IMFILESERVERIPREQ,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMFileServerIPReq)
  ))
_sym_db.RegisterMessage(IMFileServerIPReq)

IMFileServerIPRsp = _reflection.GeneratedProtocolMessageType('IMFileServerIPRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMFILESERVERIPRSP,
  __module__ = 'IM.Server_pb2'
  # @@protoc_insertion_point(class_scope:IM.Server.IMFileServerIPRsp)
  ))
_sym_db.RegisterMessage(IMFileServerIPRsp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
