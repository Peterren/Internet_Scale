class User:
    def __init__(self, user):
        if user:
            for key in user:
                setattr(self, key, user[key])
        self.is_authenticated = user is not None
