class Context:
    __instance = None
    user = None
    profile = None

    def __new__(cls, user=None, profile=None):
        if cls.__instance is None:
            if user is None or profile is None:
                raise ValueError('user and profile args are required!')
            cls.__instance = super(Context, cls).__new__(cls)
            cls.user = user
            cls.profile = profile
        return cls.__instance