number = int(input())

current_number = 1
for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(current_number, end=" ")
        current_number += 1
        if current_number > number:
            break
    print()
    if current_number > number:
        break
