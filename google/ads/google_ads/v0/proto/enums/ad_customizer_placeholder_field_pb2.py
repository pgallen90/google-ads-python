# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/ad_customizer_placeholder_field.proto

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
  name='google/ads/googleads_v0/proto/enums/ad_customizer_placeholder_field.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\nIgoogle/ads/googleads_v0/proto/enums/ad_customizer_placeholder_field.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\x8e\x01\n AdCustomizerPlaceholderFieldEnum\"j\n\x1c\x41\x64\x43ustomizerPlaceholderField\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07INTEGER\x10\x02\x12\t\n\x05PRICE\x10\x03\x12\x08\n\x04\x44\x41TE\x10\x04\x12\n\n\x06STRING\x10\x05\x42\xd2\x01\n!com.google.ads.googleads.v0.enumsB!AdCustomizerPlaceholderFieldProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_ADCUSTOMIZERPLACEHOLDERFIELDENUM_ADCUSTOMIZERPLACEHOLDERFIELD = _descriptor.EnumDescriptor(
  name='AdCustomizerPlaceholderField',
  full_name='google.ads.googleads.v0.enums.AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField',
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
      name='INTEGER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=145,
  serialized_end=251,
)
_sym_db.RegisterEnumDescriptor(_ADCUSTOMIZERPLACEHOLDERFIELDENUM_ADCUSTOMIZERPLACEHOLDERFIELD)


_ADCUSTOMIZERPLACEHOLDERFIELDENUM = _descriptor.Descriptor(
  name='AdCustomizerPlaceholderFieldEnum',
  full_name='google.ads.googleads.v0.enums.AdCustomizerPlaceholderFieldEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADCUSTOMIZERPLACEHOLDERFIELDENUM_ADCUSTOMIZERPLACEHOLDERFIELD,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=251,
)

_ADCUSTOMIZERPLACEHOLDERFIELDENUM_ADCUSTOMIZERPLACEHOLDERFIELD.containing_type = _ADCUSTOMIZERPLACEHOLDERFIELDENUM
DESCRIPTOR.message_types_by_name['AdCustomizerPlaceholderFieldEnum'] = _ADCUSTOMIZERPLACEHOLDERFIELDENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdCustomizerPlaceholderFieldEnum = _reflection.GeneratedProtocolMessageType('AdCustomizerPlaceholderFieldEnum', (_message.Message,), dict(
  DESCRIPTOR = _ADCUSTOMIZERPLACEHOLDERFIELDENUM,
  __module__ = 'google.ads.google_ads.v0.proto.enums.ad_customizer_placeholder_field_pb2'
  ,
  __doc__ = """Values for Ad Customizer placeholder fields.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.AdCustomizerPlaceholderFieldEnum)
  ))
_sym_db.RegisterMessage(AdCustomizerPlaceholderFieldEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB!AdCustomizerPlaceholderFieldProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
