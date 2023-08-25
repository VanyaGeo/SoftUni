from collections import deque

expression = deque(input().split())  # 6 3 5 - 2 1 * 5 /

idx = 0

while idx < len(expression):
    element = expression[idx]

    if element == "*":
        for _ in range(idx - 1):
            expression.appendleft(str(int(expression.popleft()) * int(expression.popleft())))
    elif element == "/":
        for _ in range(idx - 1):
            expression.appendleft(str(int(expression.popleft()) // int(expression.popleft())))
    elif element == "+":
        for _ in range(idx - 1):
            expression.appendleft(str(int(expression.popleft()) + int(expression.popleft())))
    elif element == "-":
        for _ in range(idx - 1):
            expression.appendleft(str(int(expression.popleft()) - int(expression.popleft())))

    if element in "*/+-":
        del expression[1]
        idx = 1

    idx += 1

print(int(expression[0]))


# II

# from collections import deque
# from math import floor
#
# expression = deque(input().split())  # 6 3 - 2 1 * 5 /
#
# idx = 0
#
# while idx < len(expression):
#     element = expression[idx]  # -
#
#     if element in "*/+-":
#         for _ in range(idx - 1):
#             expression.appendleft(eval(f"{int(expression.popleft())} {element} {int(expression.popleft())}"))  # 6 - 3
#
#         del expression[1]
#         idx = 1
#
#     idx += 1
#
# print(floor(int(expression[0])))