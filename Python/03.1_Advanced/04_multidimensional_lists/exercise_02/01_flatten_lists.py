string_line_list = input().split("|")
result = []
string_line_list.reverse()

for string in string_line_list:
    result.extend(string.split())

print(*result)
