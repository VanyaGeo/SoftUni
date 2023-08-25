rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_sum = float("-inf")
max_matrix = []

for row in range(rows - 2):
    current_row = []
    second_row = []
    third_row = []
    current_matrix = []
    for column in range(columns - 2):
        current_row = [matrix[row][column], matrix[row][column + 1], matrix[row][column + 2]]
        second_row = [matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2]]
        third_row = [matrix[row + 2][column], matrix[row + 2][column + 1], matrix[row + 2][column + 2]]

        current_sum = sum(current_row) + sum(second_row) + sum(third_row)
        current_matrix = [current_row, second_row, third_row]
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = current_matrix

print(f"Sum = {max_sum}")
print(*max_matrix[0], sep=" ")
print(*max_matrix[1], sep=" ")
print(*max_matrix[2], sep=" ")

# II

# rows, cols = [int(x) for x in input().split()]
# matrix = [[int(x) for x in input().split()] for row in range(rows)]
#
# max_sum = float("-inf")
# biggest_matrix = []
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         first_row = matrix[row][col:col+3]
#         second_row = matrix[row+1][col:col+3]
#         third_row = matrix[row+2][col:col+3]
#
#         current_sum = sum(first_row) + sum(second_row) + sum(third_row)
#
#         if current_sum > max_sum:
#             max_sum = current_sum
#             biggest_matrix = [first_row, second_row, third_row]
#
# print(f"Sum = {max_sum}")
# [print(*row) for row in biggest_matrix]
