rows = int(input())

matrix = []

for row in range(rows):
    inner_list = [int(x) for x in input().split()]
    matrix.append(inner_list)

primary = []
secondary = []
for row in range(rows):
    primary.append(matrix[row][row])
    secondary.append(matrix[row][rows - row - 1])

diagonal_difference = abs(sum(primary) - sum(secondary))

print(diagonal_difference)