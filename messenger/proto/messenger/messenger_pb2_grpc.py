# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import messenger_pb2 as messenger__pb2


class MessengerStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.create_thread = channel.unary_unary(
        '/messenger.Messenger/create_thread',
        request_serializer=messenger__pb2.CreateThreadRequest.SerializeToString,
        response_deserializer=messenger__pb2.CreateThreadResponse.FromString,
        )
    self.send_message = channel.unary_unary(
        '/messenger.Messenger/send_message',
        request_serializer=messenger__pb2.SendMessageRequest.SerializeToString,
        response_deserializer=messenger__pb2.SendMessageResponse.FromString,
        )
    self.get_thread_detail = channel.unary_unary(
        '/messenger.Messenger/get_thread_detail',
        request_serializer=messenger__pb2.GetThreadMessagesRequest.SerializeToString,
        response_deserializer=messenger__pb2.GetThreadDetailResponse.FromString,
        )
    self.get_thread_messages = channel.unary_unary(
        '/messenger.Messenger/get_thread_messages',
        request_serializer=messenger__pb2.GetThreadMessagesRequest.SerializeToString,
        response_deserializer=messenger__pb2.GetThreadMessagesResponse.FromString,
        )
    self.get_threads_for_user = channel.unary_unary(
        '/messenger.Messenger/get_threads_for_user',
        request_serializer=messenger__pb2.GetThreadsForUserRequest.SerializeToString,
        response_deserializer=messenger__pb2.GetThreadsForUserResponse.FromString,
        )
    self.get_message_detail = channel.unary_unary(
        '/messenger.Messenger/get_message_detail',
        request_serializer=messenger__pb2.GetMessageDetailRequest.SerializeToString,
        response_deserializer=messenger__pb2.GetMessageDetailResponse.FromString,
        )


class MessengerServicer(object):

  def create_thread(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def send_message(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get_thread_detail(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get_thread_messages(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get_threads_for_user(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get_message_detail(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessengerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'create_thread': grpc.unary_unary_rpc_method_handler(
          servicer.create_thread,
          request_deserializer=messenger__pb2.CreateThreadRequest.FromString,
          response_serializer=messenger__pb2.CreateThreadResponse.SerializeToString,
      ),
      'send_message': grpc.unary_unary_rpc_method_handler(
          servicer.send_message,
          request_deserializer=messenger__pb2.SendMessageRequest.FromString,
          response_serializer=messenger__pb2.SendMessageResponse.SerializeToString,
      ),
      'get_thread_detail': grpc.unary_unary_rpc_method_handler(
          servicer.get_thread_detail,
          request_deserializer=messenger__pb2.GetThreadMessagesRequest.FromString,
          response_serializer=messenger__pb2.GetThreadDetailResponse.SerializeToString,
      ),
      'get_thread_messages': grpc.unary_unary_rpc_method_handler(
          servicer.get_thread_messages,
          request_deserializer=messenger__pb2.GetThreadMessagesRequest.FromString,
          response_serializer=messenger__pb2.GetThreadMessagesResponse.SerializeToString,
      ),
      'get_threads_for_user': grpc.unary_unary_rpc_method_handler(
          servicer.get_threads_for_user,
          request_deserializer=messenger__pb2.GetThreadsForUserRequest.FromString,
          response_serializer=messenger__pb2.GetThreadsForUserResponse.SerializeToString,
      ),
      'get_message_detail': grpc.unary_unary_rpc_method_handler(
          servicer.get_message_detail,
          request_deserializer=messenger__pb2.GetMessageDetailRequest.FromString,
          response_serializer=messenger__pb2.GetMessageDetailResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'messenger.Messenger', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
