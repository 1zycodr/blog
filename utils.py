from exceptions import *

def option_input(string):
    result = input(string)
    if not result.isdigit():
        raise UserInputOptionException
    return result


def get_option_input():
    try:
        input_function = option_input
    except NameError:
        input_function = input

    return input_function


def username_input(string):
    result = input(string)
    if not result[0].isalpha() or len(result) < 5:
        raise InvalidUsernameException
    return result


def get_username_input():
    try:
        input_function = username_input
    except NameError:
        input_function = input

    return input_function


def password_input(string):
    result = input(string)
    if len(result) < 8:
        raise InvalidPasswordException
    return result


def get_password_input():
    try:
        input_function = password_input
    except NameError:
        input_function = input

    return input_function


def name_input(string):
    name = input(string)
    for i in name:
        if not i.isalpha():
            raise InvalidNameException
    return name


def get_name_input():
    try:
        input_function = name_input
    except NameError:
        input_function = input

    return input_function


def raise_exception(ex):
    raise ex