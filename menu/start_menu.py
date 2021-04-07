from menu import BaseMenu
from utils import get_option_input, raise_exception
from exceptions import UserInputOptionException, ExitFromMenuException
from menu.registration_menu import RegistrationMenu
from menu.login_menu import LoginMenu

class StartMenu(BaseMenu):
    __header = '-' * 10 + ' Blog ' + '-' * 10
    __options = '[1] - Sign in\n[2] - Sign up\n[3] - Exit'
    __next_menus = {
        '1': LoginMenu,
        '2': RegistrationMenu,
        '3': lambda *_: raise_exception(KeyboardInterrupt)
    }

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller

    def show(self):
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option
        
        while True:
            print(self.__header)
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
                pass