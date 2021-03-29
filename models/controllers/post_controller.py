from models.repositories import PostRepository

class PostController:
    __post_repo = None

    def __init__(self, post_repo: PostRepository):
        self.__post_repo = post_repo