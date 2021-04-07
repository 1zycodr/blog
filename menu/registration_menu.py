from menu import BaseMenu
from models import User
from utils import *

class RegistrationMenu(BaseMenu):
    header = '-' * 10 + ' Registration ' + '-' * 10

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        
    def show(self):
        input_username_func = get_username_input()
        input_password_func = get_password_input()

        def get_username():
            return input_username_func('Enter username: ')

        def get_password():
            return input_password_func('Enter password: ')

        while True:
            username = self.input_secure_wrap(get_username)
            password = self.input_secure_wrap(get_password)

            if self.__user_controller.is_user_exist(username):
                print(f'User {username} already exist!')
                continue

            profile_id = self.__profile_controller.create_empty_profile()

            if profile_id:
                user = User(username, password, profile_id)
                self.__user_controller.create_user(user)

                input(f'User {username} successfully created!\nPress Enter...')
                return
            else:
                input('Registration failed! Try again.\nPress Enter...')

            
            


