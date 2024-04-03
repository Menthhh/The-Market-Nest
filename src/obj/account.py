class User:
    def __init__(self, username, password, privileges):
        self.username = username
        self.password = password
        self.privileges = privileges

    def login(self, username, password):
        return self.username == username and self.password == password