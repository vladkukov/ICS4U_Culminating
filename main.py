import os

from Admin import Admin

print("x")
file = "UserInfo.txt"
admin = Admin("abc", "xyz", "bb", "a@b.c", file)
admin.createUserList()