# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alerts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='alerts.proto',
  package='alerts',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x61lerts.proto\x12\x06\x61lerts\"I\n\nAlertError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12*\n\nerror_code\x18\x02 \x01(\x0e\x32\x16.alerts.AlertErrorCode\"\x92\x01\n\x05\x41lert\x12\x14\n\x0crecipient_id\x18\x01 \x01(\x03\x12\x0c\n\x04uniq\x18\x02 \x01(\x03\x12\x11\n\tthread_id\x18\x03 \x01(\x03\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\x12\x13\n\x0b\x61\x63tion_path\x18\x06 \x01(\t\x12\x0b\n\x03ttl\x18\x07 \x01(\x03\x12\x0c\n\x04seen\x18\x08 \x01(\x08\"*\n\x17GetAlertsForUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\"\\\n\x18GetAlertsForUserResponse\x12\x1d\n\x06\x61lerts\x18\x01 \x03(\x0b\x32\r.alerts.Alert\x12!\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x12.alerts.AlertError\"5\n\x14MarkAlertSeenRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x0c\n\x04uniq\x18\x02 \x01(\x03\":\n\x15MarkAlertSeenResponse\x12!\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x12.alerts.AlertError\"0\n\x10SendAlertRequest\x12\x1c\n\x05\x61lert\x18\x01 \x01(\x0b\x32\r.alerts.Alert\"6\n\x11SendAlertResponse\x12!\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x12.alerts.AlertError*B\n\x0e\x41lertErrorCode\x12\r\n\tNOT_FOUND\x10\x00\x12\x10\n\x0cSERVER_ERROR\x10\x01\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x03\x32\xfb\x01\n\x06\x41lerts\x12Z\n\x13get_alerts_for_user\x12\x1f.alerts.GetAlertsForUserRequest\x1a .alerts.GetAlertsForUserResponse\"\x00\x12P\n\x0fmark_alert_seen\x12\x1c.alerts.MarkAlertSeenRequest\x1a\x1d.alerts.MarkAlertSeenResponse\"\x00\x12\x43\n\nsend_alert\x12\x18.alerts.SendAlertRequest\x1a\x19.alerts.SendAlertResponse\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ALERTERRORCODE = _descriptor.EnumDescriptor(
  name='AlertErrorCode',
  full_name='alerts.AlertErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_REQUEST', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=607,
  serialized_end=673,
)
_sym_db.RegisterEnumDescriptor(_ALERTERRORCODE)

AlertErrorCode = enum_type_wrapper.EnumTypeWrapper(_ALERTERRORCODE)
NOT_FOUND = 0
SERVER_ERROR = 1
BAD_REQUEST = 3



_ALERTERROR = _descriptor.Descriptor(
  name='AlertError',
  full_name='alerts.AlertError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='alerts.AlertError.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='alerts.AlertError.error_code', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=97,
)


_ALERT = _descriptor.Descriptor(
  name='Alert',
  full_name='alerts.Alert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipient_id', full_name='alerts.Alert.recipient_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uniq', full_name='alerts.Alert.uniq', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thread_id', full_name='alerts.Alert.thread_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='alerts.Alert.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='alerts.Alert.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_path', full_name='alerts.Alert.action_path', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='alerts.Alert.ttl', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seen', full_name='alerts.Alert.seen', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=246,
)


_GETALERTSFORUSERREQUEST = _descriptor.Descriptor(
  name='GetAlertsForUserRequest',
  full_name='alerts.GetAlertsForUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='alerts.GetAlertsForUserRequest.user_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=290,
)


_GETALERTSFORUSERRESPONSE = _descriptor.Descriptor(
  name='GetAlertsForUserResponse',
  full_name='alerts.GetAlertsForUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alerts', full_name='alerts.GetAlertsForUserResponse.alerts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='alerts.GetAlertsForUserResponse.error', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=384,
)


_MARKALERTSEENREQUEST = _descriptor.Descriptor(
  name='MarkAlertSeenRequest',
  full_name='alerts.MarkAlertSeenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='alerts.MarkAlertSeenRequest.user_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uniq', full_name='alerts.MarkAlertSeenRequest.uniq', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=439,
)


_MARKALERTSEENRESPONSE = _descriptor.Descriptor(
  name='MarkAlertSeenResponse',
  full_name='alerts.MarkAlertSeenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='alerts.MarkAlertSeenResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=441,
  serialized_end=499,
)


_SENDALERTREQUEST = _descriptor.Descriptor(
  name='SendAlertRequest',
  full_name='alerts.SendAlertRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alert', full_name='alerts.SendAlertRequest.alert', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=549,
)


_SENDALERTRESPONSE = _descriptor.Descriptor(
  name='SendAlertResponse',
  full_name='alerts.SendAlertResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='alerts.SendAlertResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=605,
)

_ALERTERROR.fields_by_name['error_code'].enum_type = _ALERTERRORCODE
_GETALERTSFORUSERRESPONSE.fields_by_name['alerts'].message_type = _ALERT
_GETALERTSFORUSERRESPONSE.fields_by_name['error'].message_type = _ALERTERROR
_MARKALERTSEENRESPONSE.fields_by_name['error'].message_type = _ALERTERROR
_SENDALERTREQUEST.fields_by_name['alert'].message_type = _ALERT
_SENDALERTRESPONSE.fields_by_name['error'].message_type = _ALERTERROR
DESCRIPTOR.message_types_by_name['AlertError'] = _ALERTERROR
DESCRIPTOR.message_types_by_name['Alert'] = _ALERT
DESCRIPTOR.message_types_by_name['GetAlertsForUserRequest'] = _GETALERTSFORUSERREQUEST
DESCRIPTOR.message_types_by_name['GetAlertsForUserResponse'] = _GETALERTSFORUSERRESPONSE
DESCRIPTOR.message_types_by_name['MarkAlertSeenRequest'] = _MARKALERTSEENREQUEST
DESCRIPTOR.message_types_by_name['MarkAlertSeenResponse'] = _MARKALERTSEENRESPONSE
DESCRIPTOR.message_types_by_name['SendAlertRequest'] = _SENDALERTREQUEST
DESCRIPTOR.message_types_by_name['SendAlertResponse'] = _SENDALERTRESPONSE
DESCRIPTOR.enum_types_by_name['AlertErrorCode'] = _ALERTERRORCODE

AlertError = _reflection.GeneratedProtocolMessageType('AlertError', (_message.Message,), dict(
  DESCRIPTOR = _ALERTERROR,
  __module__ = 'alerts_pb2'
  # @@protoc_insertion_point(class_scope:alerts.AlertError)
  ))
_sym_db.RegisterMessage(AlertError)

Alert = _reflection.GeneratedProtocolMessageType('Alert', (_message.Message,), dict(
  DESCRIPTOR = _ALERT,
  __module__ = 'alerts_pb2'
  # @@protoc_insertion_point(class_scope:alerts.Alert)
  ))
_sym_db.RegisterMessage(Alert)

GetAlertsForUserRequest = _reflection.GeneratedProtocolMessageType('GetAlertsForUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETALERTSFORUSERREQUEST,
  __module__ = 'alerts_pb2'
  # @@protoc_insertion_point(class_scope:alerts.GetAlertsForUserRequest)
  ))
_sym_db.RegisterMessage(GetAlertsForUserRequest)

GetAlertsForUserResponse = _reflection.GeneratedProtocolMessageType('GetAlertsForUserResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETALERTSFORUSERRESPONSE,
  __module__ = 'alerts_pb2'
  # @@protoc_insertion_point(class_scope:alerts.GetAlertsForUserResponse)
  ))
_sym_db.RegisterMessage(GetAlertsForUserResponse)

MarkAlertSeenRequest = _reflection.GeneratedProtocolMessageType('MarkAlertSeenRequest', (_message.Message,), dict(
  DESCRIPTOR = _MARKALERTSEENREQUEST,
  __module__ = 'alerts_pb2'
  # @@protoc_insertion_point(class_scope:alerts.MarkAlertSeenRequest)
  ))
_sym_db.RegisterMessage(MarkAlertSeenRequest)

MarkAlertSeenResponse = _reflection.GeneratedProtocolMessageType('MarkAlertSeenResponse', (_message.Message,), dict(
  DESCRIPTOR = _MARKALERTSEENRESPONSE,
  __module__ = 'alerts_pb2'
  # @@protoc_insertion_point(class_scope:alerts.MarkAlertSeenResponse)
  ))
_sym_db.RegisterMessage(MarkAlertSeenResponse)

SendAlertRequest = _reflection.GeneratedProtocolMessageType('SendAlertRequest', (_message.Message,), dict(
  DESCRIPTOR = _SENDALERTREQUEST,
  __module__ = 'alerts_pb2'
  # @@protoc_insertion_point(class_scope:alerts.SendAlertRequest)
  ))
_sym_db.RegisterMessage(SendAlertRequest)

SendAlertResponse = _reflection.GeneratedProtocolMessageType('SendAlertResponse', (_message.Message,), dict(
  DESCRIPTOR = _SENDALERTRESPONSE,
  __module__ = 'alerts_pb2'
  # @@protoc_insertion_point(class_scope:alerts.SendAlertResponse)
  ))
_sym_db.RegisterMessage(SendAlertResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class AlertsStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.get_alerts_for_user = channel.unary_unary(
          '/alerts.Alerts/get_alerts_for_user',
          request_serializer=GetAlertsForUserRequest.SerializeToString,
          response_deserializer=GetAlertsForUserResponse.FromString,
          )
      self.mark_alert_seen = channel.unary_unary(
          '/alerts.Alerts/mark_alert_seen',
          request_serializer=MarkAlertSeenRequest.SerializeToString,
          response_deserializer=MarkAlertSeenResponse.FromString,
          )
      self.send_alert = channel.unary_unary(
          '/alerts.Alerts/send_alert',
          request_serializer=SendAlertRequest.SerializeToString,
          response_deserializer=SendAlertResponse.FromString,
          )


  class AlertsServicer(object):

    def get_alerts_for_user(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def mark_alert_seen(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def send_alert(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_AlertsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'get_alerts_for_user': grpc.unary_unary_rpc_method_handler(
            servicer.get_alerts_for_user,
            request_deserializer=GetAlertsForUserRequest.FromString,
            response_serializer=GetAlertsForUserResponse.SerializeToString,
        ),
        'mark_alert_seen': grpc.unary_unary_rpc_method_handler(
            servicer.mark_alert_seen,
            request_deserializer=MarkAlertSeenRequest.FromString,
            response_serializer=MarkAlertSeenResponse.SerializeToString,
        ),
        'send_alert': grpc.unary_unary_rpc_method_handler(
            servicer.send_alert,
            request_deserializer=SendAlertRequest.FromString,
            response_serializer=SendAlertResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'alerts.Alerts', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaAlertsServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def get_alerts_for_user(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def mark_alert_seen(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def send_alert(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaAlertsStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def get_alerts_for_user(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    get_alerts_for_user.future = None
    def mark_alert_seen(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    mark_alert_seen.future = None
    def send_alert(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    send_alert.future = None


  def beta_create_Alerts_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('alerts.Alerts', 'get_alerts_for_user'): GetAlertsForUserRequest.FromString,
      ('alerts.Alerts', 'mark_alert_seen'): MarkAlertSeenRequest.FromString,
      ('alerts.Alerts', 'send_alert'): SendAlertRequest.FromString,
    }
    response_serializers = {
      ('alerts.Alerts', 'get_alerts_for_user'): GetAlertsForUserResponse.SerializeToString,
      ('alerts.Alerts', 'mark_alert_seen'): MarkAlertSeenResponse.SerializeToString,
      ('alerts.Alerts', 'send_alert'): SendAlertResponse.SerializeToString,
    }
    method_implementations = {
      ('alerts.Alerts', 'get_alerts_for_user'): face_utilities.unary_unary_inline(servicer.get_alerts_for_user),
      ('alerts.Alerts', 'mark_alert_seen'): face_utilities.unary_unary_inline(servicer.mark_alert_seen),
      ('alerts.Alerts', 'send_alert'): face_utilities.unary_unary_inline(servicer.send_alert),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Alerts_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('alerts.Alerts', 'get_alerts_for_user'): GetAlertsForUserRequest.SerializeToString,
      ('alerts.Alerts', 'mark_alert_seen'): MarkAlertSeenRequest.SerializeToString,
      ('alerts.Alerts', 'send_alert'): SendAlertRequest.SerializeToString,
    }
    response_deserializers = {
      ('alerts.Alerts', 'get_alerts_for_user'): GetAlertsForUserResponse.FromString,
      ('alerts.Alerts', 'mark_alert_seen'): MarkAlertSeenResponse.FromString,
      ('alerts.Alerts', 'send_alert'): SendAlertResponse.FromString,
    }
    cardinalities = {
      'get_alerts_for_user': cardinality.Cardinality.UNARY_UNARY,
      'mark_alert_seen': cardinality.Cardinality.UNARY_UNARY,
      'send_alert': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'alerts.Alerts', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
