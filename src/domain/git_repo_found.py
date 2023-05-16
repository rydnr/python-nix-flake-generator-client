from domain.event import Event


class GitRepoFound(Event):
    """
    Represents the event when a git repository has been found for a given Python package.
    """

    def __init__(
        self,
        packageName: str,
        packageVersion: str,
        url: str,
        tag: str
    ):
        """Creates a new GitRepoFound instance"""
        self._package_name = packageName
        self._package_version = packageVersion
        self._url = url
        self._tag = tag

    @property
    def package_name(self):
        return self._package_name

    @property
    def package_version(self):
        return self._package_version

    @property
    def url(self):
        return self._url

    @property
    def tag(self):
        return self._tag

    def __str__(self):
        return f'{{ "name": "{__name__}", "package_name": "{self.package_name}", "package_version": "{self.package_version}", "url": "{self.url}", "tag": "{self.tag}" }}'
