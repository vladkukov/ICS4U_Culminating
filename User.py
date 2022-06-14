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
        self.email = input("Enter your email: ")
        for x in userList:
            if self.email == x.email:
                password = input("Enter your password: ")
                if password == x.password:
                    print("nice")
                    return True
                else:
                    print("wrong password")
                    return False
            else:
                self.createAccount(self.email)

    @abstractmethod
    def addNewUser(self, name, email, username, password):
        pass

    def createAccount(self, email):
        self.name = input("Enter your name: ")
        self.username = input("Create a username: ")
        self.password = input("Create a password: ")
        self.addNewUser(self.name, email, self.username, self.password)
        print("\nThanks for creating an account.\n" + "Please proceed to log in \n")

    def toString(self):
        """
        name: {name}
        username: {username}
        email: {email}         
        password: {password}
        """.format(name = self.name, username = self.username, email = self.email, password = self.password)






