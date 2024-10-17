# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/transfer.proto
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
    'proto/transfer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from dictum_proto.proto import attachment_pb2 as proto_dot_attachment__pb2
from dictum_proto.proto import transfer_type_pb2 as proto_dot_transfer__type__pb2
from dictum_proto.proto import account_pb2 as proto_dot_account__pb2
from dictum_proto.proto import color_pb2 as proto_dot_color__pb2
from dictum_proto.proto import entity_pb2 as proto_dot_entity__pb2
from dictum_proto.proto import source_pb2 as proto_dot_source__pb2
from dictum_proto.proto import status_pb2 as proto_dot_status__pb2
from dictum_proto.proto import user_pb2 as proto_dot_user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14proto/transfer.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16proto/attachment.proto\x1a\x19proto/transfer_type.proto\x1a\x13proto/account.proto\x1a\x11proto/color.proto\x1a\x12proto/entity.proto\x1a\x12proto/source.proto\x1a\x12proto/status.proto\x1a\x10proto/user.proto\"\xd1\x08\n\x08Transfer\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x17\n\x0f\x63onglomerate_id\x18\x02 \x01(\x05\x12\x12\n\nis_virtual\x18\x04 \x01(\x08\x12\x17\n\x0fpayment_purpose\x18\n \x01(\t\x12\x13\n\x0bverifier_id\x18\x0e \x01(\x05\x12\x15\n\rresource_name\x18\x12 \x01(\t\x12\x0e\n\x06number\x18\x14 \x01(\t\x12\x1b\n\x04type\x18\x16 \x01(\x0e\x32\r.TransferType\x12\x17\n\x08verifier\x18\x1c \x01(\x0b\x32\x05.User\x12\x10\n\x08payer_id\x18\x1f \x01(\x05\x12\x18\n\x10payer_account_id\x18  \x01(\x05\x12\x1a\n\x12payer_transfer_key\x18! \x01(\t\x12\x14\n\x0crecipient_id\x18\" \x01(\x05\x12\x1c\n\x14recipient_account_id\x18# \x01(\x05\x12\x1e\n\x16recipient_transfer_key\x18$ \x01(\t\x12\x0e\n\x06\x61mount\x18% \x01(\x01\x12\x18\n\x10\x61llocated_amount\x18& \x01(\x01\x12\x11\n\tparent_id\x18( \x01(\x05\x12\x1b\n\ndatasource\x18* \x01(\x0e\x32\x07.Source\x12\x15\n\x05\x63olor\x18+ \x01(\x0e\x32\x06.Color\x12\x0c\n\x04note\x18, \x01(\t\x12\x1f\n\rpayer_account\x18/ \x01(\x0b\x32\x08.Account\x12#\n\x11recipient_account\x18\x30 \x01(\x0b\x32\x08.Account\x12\x16\n\x05payer\x18\x31 \x01(\x0b\x32\x07.Entity\x12\x1a\n\trecipient\x18\x32 \x01(\x0b\x32\x07.Entity\x12/\n\x0b\x63reate_time\x18\x34 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14\x66ull_allocation_time\x18\x35 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0cpayment_time\x18\x36 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bverify_time\x18\x37 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x06parent\x18\x38 \x01(\x0b\x32\t.Transfer\x12\x1f\n\x17recipient_currency_code\x18\x39 \x01(\t\x12 \n\x0b\x61ttachments\x18: \x03(\x0b\x32\x0b.Attachment\x12\x1c\n\x14payer_account_number\x18; \x01(\t\x12 \n\x18recipient_account_number\x18< \x01(\t\x12\x14\n\x0cpayer_amount\x18= \x01(\x01\x12\x18\n\x10recipient_amount\x18> \x01(\x01\x12\x1b\n\x13payer_currency_code\x18? \x01(\t\x12\x14\n\x0c\x65xternal_url\x18@ \x01(\t\x12\x17\n\x06status\x18\x41 \x01(\x0e\x32\x07.StatusB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.transfer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _globals['_TRANSFER']._serialized_start=227
  _globals['_TRANSFER']._serialized_end=1332
# @@protoc_insertion_point(module_scope)
