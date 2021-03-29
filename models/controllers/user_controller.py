from models.repositories import UserRepository

class UserController:
    __user_repo = None

    def __init__(self, user_repo: UserRepository):
        self.__user_repo = user_repo

    def create_user(self, user):
        return self.__user_repo.create_user(user)