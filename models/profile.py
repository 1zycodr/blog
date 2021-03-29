class Profile:
    __slots__ = (
        'id', 
        'first_name', 
        'second_name', 
        'last_name', 
        'age'
    )

    def __init__(
        self, 
        id = None, 
        first_name = None, 
        second_name = None,
        last_name = None, 
        age = None, 
    ):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.age = age