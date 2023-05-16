from domain.primary_port import PrimaryPort

import argparse

class ServerUrlCli(PrimaryPort):

    """
    A PrimaryPort that configures the server url from the command line.
    """

    def __init__(self):
        super().__init__()

    def priority(self) -> int:
        return 2

    async def accept(self, app):

        parser = argparse.ArgumentParser(
            description="Parses the server url"
        )
        parser.add_argument(
            "-s", "--server_url", required=True, help="The server url"
        )
        args, unknown_args = parser.parse_known_args()
        await app.accept_server_url(args.server_url)
