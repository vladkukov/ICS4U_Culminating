from User import User
from Admin import Admin

loggedIn = False

file = "UserInfo.txt"
admin = Admin("abc", "xyz", "bb", "a@b.c", file)
user = User()
admin.createUserList()
userList = admin.getUserList()

status, object = user.login(userList)

while not status:
    admin.addNewUser(user.createAccount())
    print("\nThanks for making an account, please continue to log in!\n")
    status, object = user.login(userList)
else:
    user = object



user.toString()

