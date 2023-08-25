rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
primary_diagonal = [matrix[row][row] for row in range(rows)]
secondary_diagonal = [matrix[row][rows - row - 1] for row in range(rows)]
# on each row first take the last element, then the middle element and finally the first element!!!
print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

#II

# rows = int(input())
#
# matrix = []
#
# for row in range(rows):
#     inner_list = [int(x) for x in input().split(", ")]
#     matrix.append(inner_list)
#
# primary = []
# secondary = []
# for row in range(rows):
#     primary.append(matrix[row][row])
#     secondary.append(matrix[row][rows - row - 1])
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")