from domain.git_repo_found import GitRepoFound
from domain.event import Event
from domain.event_listener import EventListener
from domain.ports import Ports

import logging

class Client():

    @classmethod
    def listenGitRepoFound(cls, event: GitRepoFound):
        server = Ports.instance().resolve(Server)
        return server.accept(event)
