rows, columns = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

matches = 0
for row in range(rows - 1):
    for column in range(columns - 1):
        current_symbol = matrix[row][column]
        right_symbol = matrix[row][column + 1]
        bottom_symbol = matrix[row + 1][column]
        diagonal_symbol = matrix[row + 1][column + 1]
        if current_symbol == right_symbol == bottom_symbol == diagonal_symbol:
            matches += 1

print(matches)
