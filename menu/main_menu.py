from menu.base_menu import BaseMenu
from menu.profile_menu import ProfileMenu
from utils import get_option_input
from models import Context
from utils import *
from exceptions import *

class MainMenu(BaseMenu):
    __header = '-' * 10 + ' Main Menu ' + '-' * 10
    __options = '[1] - Мой профиль\n[2] - Моя стена\n[3] - Лента\n[4] - Выход'
    __next_menus = {
        '1': ProfileMenu, 
        '2': lambda *_: print('not created yet'),
        '3': lambda *_: print('not created yet'),
        '4': lambda *_: raise_exception(ExitFromMenuException)
    }


    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()


    def show(self):
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.__header)
            print('You are welcome,', self.__context.user.username + '!')
            print(self.__options)  
            selected_option = self.input_secure_wrap(get_input)
            
            next_menu = self.__next_menus[selected_option](
                self.__user_controller,
                self.__profile_controller, 
                self.__post_controller
            )

            try:
                next_menu.show()
            except ExitFromMenuException:
                continue
