import pymysql

class DBService:
    instance = None
    connection = None
    cursor = None
    

    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            cls.connection = pymysql.connect(
                host='127.0.0.1',
                user='dbuser',
                password='Fks#23pq17$Dbvr',
                db='blog',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            cls.cursor = cls.connection.cursor()
        return cls.instance
    
    
    def execute(self, query):
        """
        Возвращает description запроса и исключения
        :param query: - str, запрос в бд
        :return str: - описание результата
        """
        self.cursor.execute(query)
        self.connection.commit()

        return self.cursor.description
    

    def close(self):
        """
        Закрывает все подключния с бд
        """
        if self.cursor is not None:
            self.cursor.close()

        if self.connection is not None:
            self.connection.close()


if __name__ == '__main__':
    db = Db()

# def main():
#     connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            # query = "INSERT INTO person (age, name, surname) VALUES (%d, '%s', '%s')" % (20, 'new_name', 'new_surname')
            query = "INSERT INTO person (age, name, surname) VALUES (20, %s, %s)" 
            
            cursor.execute(query, ('new_name', 'new_surname'))
            connection.commit()

            print('Description:', cursor.description)

    except Exception as ex:
        print(ex)
    finally:
        connection.close()