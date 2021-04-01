from db import DBService
from models import User
from models.repositories import UserRepository
from models.controllers import UserController
from custom_exceptions import RepositoryError


def main():
    db = DBService()
    user_repo = UserRepository(db)
    user_controller = UserController(user_repo)
    
    user = user_controller.select_user(8)

    if user is not None:
        print(user.username)
    else:
        print('none')

    
    try:
        user_controller.delete_user(user.id)
    except RepositoryError:
        print('error')

if __name__ == '__main__':
    main()