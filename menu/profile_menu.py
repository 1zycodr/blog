from menu import BaseMenu
from utils import *
from models import Context

class ProfileMenu(BaseMenu):
    __header = '-' * 10 + ' Profile ' + '-' * 10
    __options = ('[1] - Edit first name\n[2] - Edit second name\n[3] - Edit last name\n[4] - Edit age\n[5] - Exit')
    __next_menus = {}

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()
        self.__next_menus = {
            '1': self.edit_first_name,
            '2': self.edit_second_name,
            '3': self.edit_last_name, 
            '4': self.edit_age,
            '5': lambda *_: raise_exception(ExitFromMenuException)
        }


    def show(self):
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.__header)
            print(self.__context.profile)
            print(self.__options)

            selected_option = self.input_secure_wrap(get_input)

            try:
                next_menu = self.__next_menus[selected_option]()
            except ExitFromMenuException:
                return


    def edit_first_name(self):
        input_name_func = get_name_input()

        def curr_name_input():
            return input_name_func('Enter new first name: ')

        new_first_name = self.input_secure_wrap(curr_name_input)

        self.__context.profile.first_name = new_first_name

        if not self.__profile_controller.update_profile(self.__context.profile):
            print('DB error!')
        else:
            input('First name changed successfully!\nPress Enter...')


    def edit_second_name(self):
        pass


    def edit_last_name(self):
        pass


    def edit_age(self):
        pass


