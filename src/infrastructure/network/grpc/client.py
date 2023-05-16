from domain.event import Event
from domain.Server import Server

import grpc
import hello_pb2
import hello_pb2_grpc

class Client(Server):
    _server_url = None

    @classmethod
    def server_url(cls, url: str):
        cls._server_url = url

    def accept(self, event: Event):
        """
        Sends the event to the remote gRPC server.
        """
        # Create a channel to the server
        with grpc.insecure_channel(self.__class__.server_url) as channel:
            # Create a stub (client)
            stub = hello_pb2_grpc.GreeterStub(channel)

            # Create a HelloRequest message
            hello_request = hello_pb2.HelloRequest(name='Hello')

            # Use the stub to call the SayHello RPC
            response = stub.SayHello(hello_request)

            print("Greeter client received: " + response.message)
