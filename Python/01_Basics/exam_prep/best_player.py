import sys

max_score = - sys.maxsize
current_name = ""
max_name = ""
goal = 0

name = input()
while name != 'END':
    goal = int(input())
    current_name = name

    if goal > max_score:
        max_score = goal
        max_name = current_name

    if goal >= 10:
        break

    name = input()

print(f'{max_name} is the best player!')

if goal >= 3:
    print(f'He has scored {goal} goals and made a hat-trick !!!')
else:
    print(f'He has scored {goal} goals.')