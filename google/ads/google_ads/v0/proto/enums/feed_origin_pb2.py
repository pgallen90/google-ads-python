# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/feed_origin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/enums/feed_origin.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n5google/ads/googleads_v0/proto/enums/feed_origin.proto\x12\x1dgoogle.ads.googleads.v0.enums\"R\n\x0e\x46\x65\x65\x64OriginEnum\"@\n\nFeedOrigin\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x08\n\x04USER\x10\x02\x12\n\n\x06GOOGLE\x10\x03\x42\xc0\x01\n!com.google.ads.googleads.v0.enumsB\x0f\x46\x65\x65\x64OriginProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_FEEDORIGINENUM_FEEDORIGIN = _descriptor.EnumDescriptor(
  name='FeedOrigin',
  full_name='google.ads.googleads.v0.enums.FeedOriginEnum.FeedOrigin',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=106,
  serialized_end=170,
)
_sym_db.RegisterEnumDescriptor(_FEEDORIGINENUM_FEEDORIGIN)


_FEEDORIGINENUM = _descriptor.Descriptor(
  name='FeedOriginEnum',
  full_name='google.ads.googleads.v0.enums.FeedOriginEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDORIGINENUM_FEEDORIGIN,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=170,
)

_FEEDORIGINENUM_FEEDORIGIN.containing_type = _FEEDORIGINENUM
DESCRIPTOR.message_types_by_name['FeedOriginEnum'] = _FEEDORIGINENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedOriginEnum = _reflection.GeneratedProtocolMessageType('FeedOriginEnum', (_message.Message,), dict(
  DESCRIPTOR = _FEEDORIGINENUM,
  __module__ = 'google.ads.google_ads.v0.proto.enums.feed_origin_pb2'
  ,
  __doc__ = """Container for enum describing possible values for a feed origin.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.FeedOriginEnum)
  ))
_sym_db.RegisterMessage(FeedOriginEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\017FeedOriginProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)