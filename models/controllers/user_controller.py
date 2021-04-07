class UserController:
    __user_repo = None

    def __init__(self, user_repo):
        self.__user_repo = user_repo


    def create_user(self, user):
        return self.__user_repo.create_user(user)

    
    def select_user(self, id):
        return self.__user_repo.select_user(id)

    
    def is_user_exist(self, username):
        return self.__user_repo.select_user_by_username(username)

    def login_user(self, username, password):
        """
        {
            'status': 'success' / 'failed',
            'user': User / None
        }
        """

        result = {}

        user, profile = self.__user_repo.login_user(username, password)

        result['status'] = 'failed' if user is None or profile is None else 'success'
        result['user'] = user
        result['profile'] = profile 

        return result
        

    def update_user(self, user):
        return self.__user_repo.update_user(user)


    def delete_user(self, id):
        return self.__user_repo.delete_user(id)