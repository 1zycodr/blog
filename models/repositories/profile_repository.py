from db import DBService
from models import Profile

class ProfileRepository:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db