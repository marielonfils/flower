# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/task.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import node_pb2 as flwr_dot_proto_dot_node__pb2
from flwr.proto import transport_pb2 as flwr_dot_proto_dot_transport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66lwr/proto/task.proto\x12\nflwr.proto\x1a\x15\x66lwr/proto/node.proto\x1a\x1a\x66lwr/proto/transport.proto\"\xbe\x02\n\x04Task\x12\"\n\x08producer\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\"\n\x08\x63onsumer\x18\x02 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x12\n\ncreated_at\x18\x03 \x01(\t\x12\x14\n\x0c\x64\x65livered_at\x18\x04 \x01(\t\x12\x0b\n\x03ttl\x18\x05 \x01(\t\x12\x10\n\x08\x61ncestry\x18\x06 \x03(\t\x12)\n\x02sa\x18\x07 \x01(\x0b\x32\x1d.flwr.proto.SecureAggregation\x12<\n\x15legacy_server_message\x18\x65 \x01(\x0b\x32\x19.flwr.proto.ServerMessageB\x02\x18\x01\x12<\n\x15legacy_client_message\x18\x66 \x01(\x0b\x32\x19.flwr.proto.ClientMessageB\x02\x18\x01\"\\\n\x07TaskIns\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\x12\x0e\n\x06run_id\x18\x03 \x01(\x12\x12\x1e\n\x04task\x18\x04 \x01(\x0b\x32\x10.flwr.proto.Task\"\\\n\x07TaskRes\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\x12\x0e\n\x06run_id\x18\x03 \x01(\x12\x12\x1e\n\x04task\x18\x04 \x01(\x0b\x32\x10.flwr.proto.Task\"\xf3\x03\n\x05Value\x12\x10\n\x06\x64ouble\x18\x01 \x01(\x01H\x00\x12\x10\n\x06sint64\x18\x02 \x01(\x12H\x00\x12\x0e\n\x04\x62ool\x18\x03 \x01(\x08H\x00\x12\x10\n\x06string\x18\x04 \x01(\tH\x00\x12\x0f\n\x05\x62ytes\x18\x05 \x01(\x0cH\x00\x12\x33\n\x0b\x64ouble_list\x18\x15 \x01(\x0b\x32\x1c.flwr.proto.Value.DoubleListH\x00\x12\x33\n\x0bsint64_list\x18\x16 \x01(\x0b\x32\x1c.flwr.proto.Value.Sint64ListH\x00\x12/\n\tbool_list\x18\x17 \x01(\x0b\x32\x1a.flwr.proto.Value.BoolListH\x00\x12\x33\n\x0bstring_list\x18\x18 \x01(\x0b\x32\x1c.flwr.proto.Value.StringListH\x00\x12\x31\n\nbytes_list\x18\x19 \x01(\x0b\x32\x1b.flwr.proto.Value.BytesListH\x00\x1a\x1a\n\nDoubleList\x12\x0c\n\x04vals\x18\x01 \x03(\x01\x1a\x1a\n\nSint64List\x12\x0c\n\x04vals\x18\x01 \x03(\x12\x1a\x18\n\x08\x42oolList\x12\x0c\n\x04vals\x18\x01 \x03(\x08\x1a\x1a\n\nStringList\x12\x0c\n\x04vals\x18\x01 \x03(\t\x1a\x19\n\tBytesList\x12\x0c\n\x04vals\x18\x01 \x03(\x0c\x42\x07\n\x05value\"\xa0\x01\n\x11SecureAggregation\x12\x44\n\x0cnamed_values\x18\x01 \x03(\x0b\x32..flwr.proto.SecureAggregation.NamedValuesEntry\x1a\x45\n\x10NamedValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.flwr.proto.Value:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.task_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TASK'].fields_by_name['legacy_server_message']._options = None
  _globals['_TASK'].fields_by_name['legacy_server_message']._serialized_options = b'\030\001'
  _globals['_TASK'].fields_by_name['legacy_client_message']._options = None
  _globals['_TASK'].fields_by_name['legacy_client_message']._serialized_options = b'\030\001'
  _globals['_SECUREAGGREGATION_NAMEDVALUESENTRY']._options = None
  _globals['_SECUREAGGREGATION_NAMEDVALUESENTRY']._serialized_options = b'8\001'
  _globals['_TASK']._serialized_start=89
  _globals['_TASK']._serialized_end=407
  _globals['_TASKINS']._serialized_start=409
  _globals['_TASKINS']._serialized_end=501
  _globals['_TASKRES']._serialized_start=503
  _globals['_TASKRES']._serialized_end=595
  _globals['_VALUE']._serialized_start=598
  _globals['_VALUE']._serialized_end=1097
  _globals['_VALUE_DOUBLELIST']._serialized_start=953
  _globals['_VALUE_DOUBLELIST']._serialized_end=979
  _globals['_VALUE_SINT64LIST']._serialized_start=981
  _globals['_VALUE_SINT64LIST']._serialized_end=1007
  _globals['_VALUE_BOOLLIST']._serialized_start=1009
  _globals['_VALUE_BOOLLIST']._serialized_end=1033
  _globals['_VALUE_STRINGLIST']._serialized_start=1035
  _globals['_VALUE_STRINGLIST']._serialized_end=1061
  _globals['_VALUE_BYTESLIST']._serialized_start=1063
  _globals['_VALUE_BYTESLIST']._serialized_end=1088
  _globals['_SECUREAGGREGATION']._serialized_start=1100
  _globals['_SECUREAGGREGATION']._serialized_end=1260
  _globals['_SECUREAGGREGATION_NAMEDVALUESENTRY']._serialized_start=1191
  _globals['_SECUREAGGREGATION_NAMEDVALUESENTRY']._serialized_end=1260
# @@protoc_insertion_point(module_scope)
