from User import User

class Admin(User):
    def __init__(self, username, password, name, email, userInfo):
        User.__init__(self, username, password, name, email)
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.userInfo = userInfo
        self.userList = []

# creates users from file and appends references to a list
    def createUserList(self):
        infoFile = open(self.userInfo, "r")
        lists = [[],[],[],[]]
        length = 0
        for line in infoFile:
            lists[length].append(line.strip())
            length+=1
            if length == 4:
                length = 0

        for i in range((len(lists[1]))-1):
            self.userList.append(User(lists[0][i], lists[1][i], lists[2][i], lists[3][i]))




