def is_valid_index(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


rows = int(input())

matrix = [[int(x) for x in input().split()] for row in range(rows)]

command = input().split()
while command[0] != "END":
    command_type, row, column, value = command[0], int(command[1]), int(command[2]), int(command[3])
    if is_valid_index(matrix, row, column):
        if command_type == "Add":
            matrix[row][column] += value
        elif command_type == "Subtract":
            matrix[row][column] -= value
    else:
        print("Invalid coordinates")

    command = input().split()

# for row in matrix:
#     print(" ".join(str(x) for x in row))

# print('\n'.join([' '.join(map(str, row)) for row in matrix]))

[print(*row) for row in matrix]


