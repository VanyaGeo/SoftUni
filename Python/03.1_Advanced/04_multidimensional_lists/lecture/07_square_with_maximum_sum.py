rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    matrix.append(inner_list)

current_sum_elements = 0
max_sum_matrix = []

for row in range(rows - 1):
    for column in range(columns - 1):
        current_element = matrix[row][column]
        right_element = matrix[row][column + 1]
        bottom_element = matrix[row + 1][column]
        diagonal_element = matrix[row + 1][column + 1]
        sum_elements = current_element + right_element + bottom_element + diagonal_element
        if sum_elements > current_sum_elements:
            current_sum_elements = sum_elements
            max_sum_matrix = [[current_element, right_element], [bottom_element, diagonal_element]]

print(*max_sum_matrix[0])
print(*max_sum_matrix[1])
print(current_sum_elements)

