def is_valid_move(matrix, r, c):
    rows_matrix = len(matrix)
    columns_matrix = len(matrix[0])
    return 0 <= r < rows_matrix and 0 <= c < columns_matrix


rows, cols = [int(x) for x in input().split(",")]
matrix = []
mouse_position = []

for row in range(rows):
    inner_list = [x for x in input()]
    matrix.append(inner_list)
    if "M" in matrix[row]:
        mouse_position = [row, matrix[row].index("M")]
        matrix[row][mouse_position[1]] = "*"


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row = mouse_position[0]
column = mouse_position[1]

command = input()
while command:
    cheese_count = sum(row.count("C") for row in matrix)

    previous_row = row
    previous_column = column

    if command == "danger":
        row = previous_row
        column = previous_column
        matrix[row][column] = "M"
        print("Mouse will come back later!")
        for r in matrix:
            print(''.join(r))
        exit()

    new_row = directions[command][0]
    new_column = directions[command][1]

    row += new_row
    column += new_column

    if not is_valid_move(matrix, row, column):
        print("No more cheese for tonight!")
        row = previous_row
        column = previous_column
        matrix[row][column] = "M"
        for r in matrix:
            print(''.join(r))
        exit()

    if matrix[row][column] == "@":
        row = previous_row
        column = previous_column

    if matrix[row][column] == "C":
        matrix[row][column] = "*"
        cheese_count -= 1
        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            matrix[row][column] = "M"
            for r in matrix:
                print(''.join(r))
            exit()

    if matrix[row][column] == "T":
        # row = previous_row
        # column = previous_column
        matrix[row][column] = "M"
        print("Mouse is trapped!")
        for r in matrix:
            print(''.join(r))
        exit()

    command = input()
