from domain.event import Event
from domain.server import Server

import infrastructure.network.grpc.git_repo_found_pb2 as git_repo_found_pb2
import infrastructure.network.grpc.git_repo_found_pb2_grpc as git_repo_found_pb2_grpc

import grpc
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
        logging.getLogger(__name__).debug(f"Sending event {event} to server {self.__class__.server_url}")
        # Create a channel to the server
        with grpc.insecure_channel(self.__class__._server_url) as channel:
            # Create a stub (client)
            stub = git_repo_found_pb2_grpc.GitRepoFoundServiceStub(channel)

            # Create a GitRepoFound message
            git_repo_found = git_repo_found_pb2.GitRepoFound(package_name=event.package_name, package_version=event.package_version, url=event.url, tag=event.tag)

            # Use the stub to notify of GitRepoFound events
            response = stub.GitRepoFoundNotifications(git_repo_found)
