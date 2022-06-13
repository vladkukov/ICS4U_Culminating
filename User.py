class User:
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def login(self):
        email = input("Enter your email: ")
        if email in self.userList:
            password = input("Enter your password")
        else:
            self.createAccount(email)

    def createAccount(self, email):
        self.name = input("Enter your name: ")
        self.username = input("Create a username: ")
        self.password = input("Create a password: ")




