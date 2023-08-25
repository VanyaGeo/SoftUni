width = int(input())
length = int(input())
height = int(input())
area = width * length * height
left = area

user_input = input()

while user_input != "Done":
    boxes = int(user_input)
    left = left - boxes
    if left <= 0:
        diff = abs(left)
        print(f"No more free space! You need {diff} Cubic meters more.")
        break

    user_input = input()

if user_input == "Done":
    print(f"{left} Cubic meters left.")
