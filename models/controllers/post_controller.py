class PostController:
    __post_repo = None

    def __init__(self, post_repo):
        self.__post_repo = post_repo