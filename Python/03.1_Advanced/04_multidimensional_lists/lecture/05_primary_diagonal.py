# rows = int(input())
#
# matrix = []
#
# for row in range(rows):
#     inner_list = [int(x) for x in input().split()]
#     matrix.append(inner_list)
#
# sum_primary_diagonal = 0
#
# for row_index in range(rows):
#     sum_primary_diagonal += matrix[row_index][row_index]
#
# print(sum_primary_diagonal)


#II

sum_diagonal = 0
for i in range(int(input())):
    sum_diagonal += [int(i) for i in input().split()][i]

print(sum_diagonal)
