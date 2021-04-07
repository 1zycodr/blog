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

    @classmethod
    def from_dict(cls, data):
        return Profile(**data)

    def __str__(self):
        fname, sname, lname, age = (
            self.first_name, 
            self.second_name, 
            self.last_name, 
            self.age
        )

        if fname is None or fname == 'None':
            fname = 'Не задано'
        
        if sname is None or sname == 'None':
            sname = 'Не задано'

        if lname is None or lname == 'None':
            lname = 'Не задано'

        if age is None or age == 'None':
            age = 'Не задано'

        return f"First name: {fname}\nSecond name: {sname}\nLast name: {lname}\nAge: {age}"
    
    