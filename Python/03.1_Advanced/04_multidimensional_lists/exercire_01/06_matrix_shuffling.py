def is_valid_index(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


rows, columns = [int(x) for x in input().split()]

matrix = [input().split() for row in range(rows)]

command = input()
while command != "END":
    data = command.split()
    if len(data) == 5 and data[0] == "swap":
        row_1 = int(data[1])
        col_1 = int(data[2])
        row_2 = int(data[3])
        col_2 = int(data[4])
        if is_valid_index(matrix, row_1, col_1) and is_valid_index(matrix, row_2, col_2):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]

            [print(*row) for row in matrix]

        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input()

# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
