from domain.git_repo_found import GitRepoFound

class Server():

    def accept(self, event: GitRepoFound):
        """
        Accepts a GitRepoFound event.
        """
        raise NotImplementedError("accept(event) not implemented by the subclass")
