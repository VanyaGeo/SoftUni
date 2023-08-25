# matrix = [[1, 2, 3], [4, 5, 6]]
# flattening = [num for sublist in matrix for num in sublist]

# ==>for row_index in range(len(matrix)):
#     for column_index in range(len(matrix[row_index])):
#         current_element = matrix[row_index][column_index]
#         flattening.append(current_element)

# ==> for list_element in matrix:
#     flattening.extend(list_element)


row = int(input())

matrix = []

for row_index in range(row):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)

flatten = []

for row_index in range(row):
    for column_index in range(len(matrix[row_index])):
        flatten.append(matrix[row_index][column_index])

print(flatten)

# II

# row = int(input())
#
# flatten = []
#
# for row_index in range(row):
#     inner_list = [int(el) for el in input().split(", ")]
#     flatten.extend(inner_list)
#
# print(flatten)