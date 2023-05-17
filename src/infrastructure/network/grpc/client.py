from domain.event import Event
from domain.server import Server

import grpc
import hello_pb2
import hello_pb2_grpc
import logging

class Client(Server):
    _server_url = None

    @classmethod
    def server_url(cls, url: str):
        cls._server_url = url

    async def accept(self, event: Event):
        """
        Sends the event to the remote gRPC server.
        """
        logging.getLogger(__name__).debug(f"Sending Hello to server {self.__class__.server_url}")
        # Create a channel to the server
        with grpc.insecure_channel(self.__class__._server_url) as channel:
            # Create a stub (client)
            stub = hello_pb2_grpc.GreeterStub(channel)

            # Create a HelloRequest message
            hello_request = hello_pb2.HelloRequest(name='Hello')

            # Use the stub to call the SayHello RPC
            response = stub.SayHello(hello_request)

            print("Greeter client received: " + response.message)
