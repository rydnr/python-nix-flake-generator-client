from domain.event import Event
from domain.event_listener import EventListener
from domain.git.git_repo_found import GitRepoFound
from domain.ports import Ports
from domain.server import Server

import logging
from typing import List, Type

class Client(EventListener):

    @classmethod
    def supported_events(cls) -> List[Type[Event]]:
        """
        Retrieves the list of supported event classes.
        """
        return [ GitRepoFound ]


    @classmethod
    def listenGitRepoFound(cls, event: GitRepoFound):

        server = Ports.instance().resolve(Server)
        return server.acceptGitRepoFound(event)
