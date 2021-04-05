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
        