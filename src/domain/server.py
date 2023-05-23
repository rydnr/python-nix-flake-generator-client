from domain.git.git_repo_found import GitRepoFound
from domain.port import Port

class Server(Port):

    def acceptGitRepoFound(self, event: GitRepoFound):
        """
        Accepts a GitRepoFound event.
        """
        raise NotImplementedError("acceptGitRepoFound() not implemented by the subclass")
