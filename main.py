from User import User
from Admin import Admin

loggedIn = False

file = "UserInfo.txt"
admin = Admin("abc", "xyz", "bb", "a@b.c", file)
user = User()
admin.createUserList()
userList = admin.getUserList()
while not loggedIn:
    loggedIn = admin.login(userList)
