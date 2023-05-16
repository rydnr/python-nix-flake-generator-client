#!/usr/bin/env python3

from application.bootstrap import get_interfaces, get_implementations

import asyncio
import importlib
import importlib.util
import logging
import os
from typing import Dict, List

class PythonNixFlakeGeneratorClient():

    _singleton = None

    def __init__(self):
        super().__init__()
        self._primaryPorts = []

    def get_primary_ports(self):
        return self._primaryPorts

    @classmethod
    def initialize(cls):
        cls._singleton = PythonNixFlakeGeneratorClient()
        mappings = {}
        for port in cls.get_port_interfaces():
            # this is to pass the infrastructure module, so I can get rid of the `import infrastructure`
            infrastructureModule = importlib.import_module('.'.join(configure_logging.__module__.split('.')[:-1]))
            implementations = get_implementations(port, infrastructureModule)
            if len(implementations) == 0:
                logging.getLogger(__name__).critical(f'No implementations found for {port}')
            else:
                mappings.update({ port: implementations[0]() })
        Ports.initialize(mappings)
        cls._singleton._primaryPorts = get_implementations(PrimaryPort, infrastructureModule)
        EventListener.find_listeners()

    @classmethod
    def get_port_interfaces(cls):
        # this is to pass the domain module, so I can get rid of the `import domain`
        return get_interfaces(Port, importlib.import_module('.'.join(Event.__module__.split('.')[:-1])))

    @classmethod
    def instance(cls):
        return cls._singleton

    @classmethod
    def delegate_priority(cls, primaryPort) -> int:
        return primaryPort().priority()

    async def accept_input(self):
        for primaryPort in sorted(self.get_primary_ports(), key=PythonNixFlakeGeneratorClient.delegate_priority):
            port = primaryPort()
            await port.accept(self)

    async def accept(self, event): # : Event) -> Event:
        result = []
        if event:
            firstEvents = []
            logging.getLogger(__name__).info(f'Accepting event {event}')
            for listenerClass in EventListener.listeners_for(event.__class__):
                resultingEvents = await listenerClass.accept(listenerClass, event)
                if resultingEvents and len(resultingEvents) > 0:
                    firstEvents.extend(resultingEvents)
            if len(firstEvents) > 0:
                result.extend(firstEvents)
                for event in firstEvents:
                    result.extend(await self.accept(event))
        return result

    async def accept_configure_logging(self, logConfig: Dict[str, bool]):
        for module_functions in self.get_log_configs():
            module_functions(logConfig["verbose"], logConfig["trace"], logConfig["quiet"])

    def get_log_configs(self) -> List[Dict]:
        result = []

        spec = importlib.util.spec_from_file_location("_log_config", os.path.join("src", os.path.join("infrastructure", f"_log_config.py")))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        entry = {}
        configure_logging_function = getattr(module, "configure_logging", None)
        if callable(configure_logging_function):
            result.append(configure_logging_function)
        else:
            print(f"Error in src/infrastructure/_log_config.py: configure_logging")
        return result

if __name__ == "__main__":

    from domain.event import Event
    from domain.event_listener import EventListener
    from domain.port import Port
    from domain.ports import Ports
    from domain.primary_port import PrimaryPort
    from infrastructure._log_config import configure_logging

    PythonNixFlakeGeneratorClient.initialize()
    PythonNixFlakeGeneratorClient.instance().accept_input()
