class Post:
    __slots__ = (
        'id', 
        'creation_date', 
        'updated_at', 
        'user_id', 
        'title', 
        'description'
    )

    def __init__(
        self, 
        user_id, 
        title, 
        id = None, 
        creation_date = None, 
        updated_at = None,
        description = None
    ):
        self.id = id
        self.user_id = user_id
        self.creation_date = creation_date
        self.updated_at = updated_at
        self.title = title
        self.description = description
