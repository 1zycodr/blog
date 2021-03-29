class User:
    __slots__ = ('id', 'creation_date', 'username', 'password', 'profile_id')

    def __init__(
        self, 
        username,  
        password, 
        profile_id,
        id = None, 
        creation_date = None
    ):
        self.id = id
        self.creation_date = creation_date
        self.username = username
        self.password = password
        self.profile_id = profile_id