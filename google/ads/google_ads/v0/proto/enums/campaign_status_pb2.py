# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/campaign_status.proto

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
  name='google/ads/googleads_v0/proto/enums/campaign_status.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n9google/ads/googleads_v0/proto/enums/campaign_status.proto\x12\x1dgoogle.ads.googleads.v0.enums\"j\n\x12\x43\x61mpaignStatusEnum\"T\n\x0e\x43\x61mpaignStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07\x45NABLED\x10\x02\x12\n\n\x06PAUSED\x10\x03\x12\x0b\n\x07REMOVED\x10\x04\x42\xc4\x01\n!com.google.ads.googleads.v0.enumsB\x13\x43\x61mpaignStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_CAMPAIGNSTATUSENUM_CAMPAIGNSTATUS = _descriptor.EnumDescriptor(
  name='CampaignStatus',
  full_name='google.ads.googleads.v0.enums.CampaignStatusEnum.CampaignStatus',
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
      name='ENABLED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVED', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=114,
  serialized_end=198,
)
_sym_db.RegisterEnumDescriptor(_CAMPAIGNSTATUSENUM_CAMPAIGNSTATUS)


_CAMPAIGNSTATUSENUM = _descriptor.Descriptor(
  name='CampaignStatusEnum',
  full_name='google.ads.googleads.v0.enums.CampaignStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CAMPAIGNSTATUSENUM_CAMPAIGNSTATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=198,
)

_CAMPAIGNSTATUSENUM_CAMPAIGNSTATUS.containing_type = _CAMPAIGNSTATUSENUM
DESCRIPTOR.message_types_by_name['CampaignStatusEnum'] = _CAMPAIGNSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignStatusEnum = _reflection.GeneratedProtocolMessageType('CampaignStatusEnum', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNSTATUSENUM,
  __module__ = 'google.ads.google_ads.v0.proto.enums.campaign_status_pb2'
  ,
  __doc__ = """Container for enum describing possible statuses of a campaign.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.CampaignStatusEnum)
  ))
_sym_db.RegisterMessage(CampaignStatusEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\023CampaignStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
