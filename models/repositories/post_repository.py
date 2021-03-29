from db import DBService
from models import Post

class PostRepository:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db