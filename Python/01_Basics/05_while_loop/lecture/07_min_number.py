import sys

user_input = input()
min_num = sys.maxsize

while user_input != "Stop":
    number = int(user_input)
    if number < min_num:
        min_num = number

    user_input = input()

print(min_num)
