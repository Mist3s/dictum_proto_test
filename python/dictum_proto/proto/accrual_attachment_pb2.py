# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/accrual_attachment.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'proto/accrual_attachment.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dictum_proto.proto import attachment_pb2 as proto_dot_attachment__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eproto/accrual_attachment.proto\x1a\x16proto/attachment.proto\"~\n\x11\x41\x63\x63rualAttachment\x12\x1d\n\x15\x61\x63\x63rual_attachment_id\x18\x01 \x01(\x05\x12\x15\n\rattachment_id\x18\x02 \x01(\x05\x12\x12\n\naccrual_id\x18\x03 \x01(\x05\x12\x1f\n\nattachment\x18\x04 \x01(\x0b\x32\x0b.AttachmentB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.accrual_attachment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _globals['_ACCRUALATTACHMENT']._serialized_start=58
  _globals['_ACCRUALATTACHMENT']._serialized_end=184
# @@protoc_insertion_point(module_scope)
