class ProfileController:
    __profile_repo = None

    def __init__(self, profile_repo):
        self.__profile_repo = profile_repo

    def select_profile(self, id):
        return self.__profile_repo.select_profile(id)