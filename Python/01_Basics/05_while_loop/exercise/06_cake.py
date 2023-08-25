a = int(input())
b = int(input())
area = a * b
left = area
user_input = input()


while user_input != "STOP":
    pieces = int(user_input)
    left = left - pieces

    if left < 0:
        diff = abs(left)
        print(f"No more cake left! You need {diff} pieces more.")
        break

    user_input = input()

if user_input == "STOP":
    print(f"{left} pieces are left." )
