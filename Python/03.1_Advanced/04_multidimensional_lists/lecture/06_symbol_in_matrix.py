rows = int(input())

matrix = []

for row in range(rows):
    inner_list = list(input())
    # inner_list = [char for char in input().split()]
    matrix.append(inner_list)

searched_element = input()
found_position = ()

for row in range(rows):
    if found_position:
        break
    for column in range(len(matrix[row])):
        if searched_element == matrix[row][column]:
            found_position = (row, column)
            break

if found_position:
    print(found_position)
else:
    print(f"{searched_element} does not occur in the matrix")
