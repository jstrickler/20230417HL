
import sys
import os.path

if sys.platform == 'win32':
    user_key = 'USERNAME'
else:
    user_key = 'USER'

count_key = 'COUNT'

os.environ[count_key] = "42"  # set environment variable
print("count is", os.environ[count_key], "user is", os.environ[user_key])  # os.environ is a dictionary
print("count is", os.environ.get(count_key), "user is", os.environ.get(user_key))  # os.environ.get() is safer than os.environ[]
user = os.getenv(user_key)  # os.getenv() is shortcut for os.environ.get()
count = os.getenv(count_key)
print("count is", count, "user is", user)
cmd = "count is ${} user is ${}".format(count_key, user_key)
print("cmd:", cmd)
print(os.path.expandvars(cmd))  # expand variables in place; handy for translating shell scripts
