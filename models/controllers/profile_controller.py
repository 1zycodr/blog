from models.repositories import ProfileRepository

class ProfileController:
    __profile_repo = None

    def __init__(self, profile_repo: ProfileRepository):
        self.__profile_repo = profile_repo