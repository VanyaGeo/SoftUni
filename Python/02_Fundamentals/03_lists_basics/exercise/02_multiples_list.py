factor = int(input())
count = int(input())
list_of_number_result = []

for number in range(1, count + 1):
    result = number * factor
    list_of_number_result.append(result)

print(list_of_number_result)
