numbers_list = input().split()
numbers_to_remove = int(input())
numbers_list_as_digits = []
numbers_list_as_string = []

for element in range(len(numbers_list)):
    numbers_list_as_digits.append(int(numbers_list[element]))
    # ==> numbers_list_as_digits[element] = int(numbers_list[element])

for i in range(numbers_to_remove):
    min_number = min(numbers_list_as_digits)
    numbers_list_as_digits.remove(min_number)

for element in range(len(numbers_list_as_digits)):
    numbers_list_as_string.append(str(numbers_list_as_digits[element]))
    # ==> numbers_list_as_string[element] = str(numbers_list_as_digits[element])

result = ", ".join(numbers_list_as_string)
print(result)
