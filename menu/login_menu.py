from menu import BaseMenu
from menu.main_menu import MainMenu
from utils import get_option_input, raise_exception
from exceptions import ExitFromMenuException
from models import Context

class LoginMenu(BaseMenu):
    __header = '-' * 10 + ' Login ' + '-' * 10
    __options = '[1] - Retry\n[2] - Back'
    
    
    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller

        self.__next_menus = {
            '1': lambda *_: None,
            '2': lambda *_: raise_exception(ExitFromMenuException)
        }

    def show(self):
        print(self.__header)

        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            username = input('Enter username: ')
            password = input('Enter password: ')

            context = self.__user_controller.login_user(username, password)

            if context['status'] == 'success': 
                menu_context = Context(context['user'], context['profile'])
                next_menu = MainMenu(
                    self.__user_controller,
                    self.__profile_controller, 
                    self.__post_controller
                )
                next_menu.show()
            elif context['status'] == 'failed':
                print('Login error!')
                print(self.__options)

                selected_option = self.input_secure_wrap(get_input)

                try:
                    self.__next_menus[selected_option](
                        self.__user_controller,
                        self.__profile_controller, 
                        self.__post_controller
                    )
                except ExitFromMenuException:
                    return

        
        