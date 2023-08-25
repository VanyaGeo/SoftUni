import sys

user_input = input()
max_num = -sys.maxsize

while user_input != "Stop":
    number = int(user_input)
    if number > max_num:
        max_num = number

    user_input = input()

print(max_num)
