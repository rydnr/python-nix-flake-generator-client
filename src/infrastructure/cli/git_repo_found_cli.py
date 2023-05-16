from domain.git_repo_found import GitRepoFound
from domain.primary_port import PrimaryPort

import argparse
import logging


class GitRepoFoundCli(PrimaryPort):

    """
    A PrimaryPort that sends GitRepoFound events specified from the command line.
    """
    def priority(self) -> int:
        return 100

    async def accept(self, app):

        parser = argparse.ArgumentParser(
            description="Sends the git repository for a given Python package"
        )
        parser.add_argument("type", choices=['git_repo_found'], nargs='?', default=None, help="The type of event to send")
        parser.add_argument("packageName", help="The name of the Python package")
        parser.add_argument("packageVersion", help="The version of the Python package")
        parser.add_argument("url", help="The url of the git repository")
        args, unknown_args = parser.parse_known_args()

        if args.type == "git_repo_found":
            event = GitRepoFound(args.packageName, args.packageVersion, args.url)
            logging.getLogger(__name__).debug(f"Notifying the url of the git repository of {event.package_name}-{event.package_version} is {args.url}")
            await app.accept(event)
