def string_into_digits(nums):
    list_of_numbers = []
    for digits in nums:
        list_of_numbers.append(int(digits))
    sorted_list = sorted(list_of_numbers)
    return sorted_list


numbers = input().split()
result = string_into_digits(numbers)
print(result)
