# greet_user.py
import sys


def greet_users(usernames):
    if usernames[0]:
        usernames = usernames[0].upper()+usernames[1:]
    return usernames


args = sys.argv[1:]
for i in args:
    print("Hello, " + greet_users(i) + "!")

