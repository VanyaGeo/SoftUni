rows, columns = [int(x) for x in input().split(", ")]

matrix = []
column_sum_elements = []

for row_index in range(rows):
    inner_list = [int(x) for x in input().split()]
    matrix.append(inner_list)

for column_index in range(columns):
    sum_nums = 0
    for row_index in range(rows):
        sum_nums += matrix[row_index][column_index]
    column_sum_elements.append(sum_nums)

print(*column_sum_elements, sep="\n")
