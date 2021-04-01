from db import DBService
from models import User
from custom_exceptions import RepositoryError

class UserRepository:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db
        

    def create_user(self, user: User):
        """
        Выполняет добавление пользователя в бд. 
        :param user: - User
        :raise RepositoryError: - ошибка в бд
        """

        try:
            query = "INSERT INTO blog_user (username, password, profile_id) VALUES ('{username}', '{password}', {profile_id})"
            query = query.format(
                username = user.username, 
                password = user.password,
                profile_id = user.profile_id
            )
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError

    
    def select_user(self, id):
        """
        Возвращает объект класса User с бд с нужным нам id
        :param id: - int
        :return User: - успешный select (такая запись есть)
        :return None: - такой записи нету
        :raise RepositoryError: - ошибка в бд
        """

        try:
            query = "SELECT * FROM blog_user WHERE id = %d" % id
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                return User.from_dict(self.__db.cursor.fetchone())
            else:
                return None
        except Exception as ex:
            print(ex)
            raise RepositoryError

    
    def update_user(self, user: User):
        """
        ОБновляет данные пользователя по его id
        :param user: - User
        :raise RepositoryError: - ошибка в бд
        """

        try:
            query = "UPDATE blog_user SET username = '{username}', password = '{password}', profile_id = {profile_id} WHERE id = {id}"
            query = query.format(
                id = user.id,
                username = user.username,
                password = user.password,
                profile_id = user.profile_id
            )
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError

    
    def delete_user(self, id):
        """
        Удалять пользователя по его id
        :param id: - id
        :raise RepositoryError: - ошибка в бд
        """

        try:
            query = "DELETE FROM blog_user WHERE id = %d" % id
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError