rows, columns = input().split(", ")
matrix = []

for element in range(int(rows)):
    num = [int(x) for x in input().split(", ")]
    matrix.append(num)

sum_nums = 0

for row_index in range(int(rows)):
    for column_index in range(int(columns)):
        sum_nums += matrix[row_index][column_index]

print(sum_nums)
print(matrix)