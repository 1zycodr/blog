from menu import BaseMenu
from utils import get_option_input

class RegistrationMenu(BaseMenu):
    header = '-' * 10 + ' Registration ' + '-' * 10
    options = ''
    next_menus = {
        
    }

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        
    def show(self):
        pass