from abc import abstractmethod


class User:
    def __init__(self, name="", email="", username="", password=""):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def login(self, userList):
        password = None
        self.email = input("Enter your email: ")
        for x in userList:
            if self.email == x.email:
                while password != x.password:
                    password = input("Enter your password: ")
                    if password != x.password:
                        print("wrong password")
                print("right password")
                return True, x
        print("Email not found, please create an account \n")
        return False, None

    @abstractmethod
    def addNewUser(self, name, email, username, password):
        pass

    def createAccount(self):
        self.email = input("Enter your email: ")
        self.name = input("Enter your name: ")
        self.username = input("Create a username: ")
        self.password = input("Create a password: ")
        return [self.name, self.email, self.username, self.password]
        print("\nThanks for creating an account.\n" + "Please proceed to log in \n")

    def toString(self):
        print(
            "\nname: " + self.name,
            "\nusername: " + self.username,
            "\nemail: " + self.email,
            "\npassword: " + self.password
        )
