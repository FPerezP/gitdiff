class Author:
    def __init__(self, email, name):
        self.email = email
        self.name = name

    def __str__(self):
        return self.name + ', ' + self.email