import os

from Admin import Admin

print(os.chdir("C:/Users/jrond/PycharmProjects/ICS4U_Culminating"))
print("x")
file = "UserInfo.txt"
admin = Admin("abc", "xyz", "bb", "a@b.c", file)
admin.createUserList()