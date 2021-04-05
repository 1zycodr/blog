from menu import BaseMenu
from utils import get_option_input
from models import Context

class MainMenu(BaseMenu):
    __header = '-' * 10 + ' Main Menu ' + '-' * 10
    __options = ''
    __next_menus = {
        
    }


    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()


    def show(self):
        print(self.__header)
        print('You are welcome,', self.__context.user.username, self.__context.profile.last_name)