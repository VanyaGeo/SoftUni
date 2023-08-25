row = int(input())
matrix = [[int(element) for element in input().split(", ") if int(element) % 2 == 0] for row_index in range(row)]
#
# for row_index in range(row):
#     inner_list = [int(element) for element in input().split(", ") if int(element) % 2 == 0]
#     matrix.append(inner_list)

print(matrix)