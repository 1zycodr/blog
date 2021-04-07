from db import DBService
from models import Profile

class ProfileRepository:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db

    
    def select_profile(self, id):
        """
        Возвращает объект класса Profile с бд с нужным нам id
        :param id: - int
        :return Profile: - успешный select (такая запись есть)
        :return None: - такой записи нету
        :raise RepositoryError: - ошибка в бд
        """

        try:
            query = "SELECT * FROM profile WHERE id = %d" % id
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                return Profile.from_dict(self.__db.cursor.fetchone())
            else:
                return None
                
        except Exception as ex:
            print(ex)
            raise RepositoryError
        

    def create_empty_profile(self):
        """
        Создает пустой профиль и возвращает его id
        """

        try:
            # создаём профиль
            query = "INSERT INTO profile () VALUES ();"
            self.__db.execute(query)

            # получаем его id
            query = "SELECT max(id) as id FROM profile;"
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                return self.__db.cursor.fetchone()['id']
            else:
                return None
                
        except Exception as ex:
            print(ex)
            raise RepositoryError


    def update_profile(self, profile):
        """
        Обновляет данные профиля
        """
        try:
            query = "UPDATE profile SET first_name = '{first_name}', second_name = '{second_name}', last_name = '{last_name}', age = {age} WHERE id = {id}"
            query = query.format(
                id = profile.id,
                first_name = profile.first_name, 
                second_name = profile.second_name,
                last_name = profile.last_name, 
                age = profile.age if profile.age is not None else 'NULL'
            )

            self.__db.execute(query)

            return True

        except Exception as ex:
            print(ex)
            return False