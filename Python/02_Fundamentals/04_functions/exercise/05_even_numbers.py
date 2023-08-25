# I
# def even_numbers(nums):
#     list_of_even_numbers = []
#     for digit in nums:
#         if int(digit) % 2 == 0:
#             list_of_even_numbers.append(int(digit))
#         else:
#             continue
#     return list_of_even_numbers
#
#
# numbers = input().split()
# final_result = even_numbers(numbers)
# print(final_result)

# II
# def even_numbers(nums):
#     for digit in nums:
#         if int(digit) % 2 == 0:
#             return True
#         else:
#             return False
#
#
# numbers = input().split()
# result_of_even_numbers = filter(even_numbers, numbers)
# list_result_of_even_numbers = list(result_of_even_numbers)
# list_integers = [int(x) for x in list_result_of_even_numbers]
#
# print(list_integers)

# III
#
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False   # == else: return False
#
#
# numbers = input().split()
# filtered_numbers = []
# for current_number in numbers:
#     if is_even(current_number):
#         filtered_numbers.append(int(current_number))
#
# print(filtered_numbers)


# IV

# numbers_as_digits = [int(x) for x in input().split() if x % 2 == 0] # цялата задача в един ред

# numbers_as_string = input().split()
# numbers_as_digits = []
# for current_number in numbers_as_string:
#     if int(current_number) % 2 == 0:
#         numbers_as_digits.append(int(current_number)) # == дълъг вариант на горното записване

numbers_as_digits = [int(x) for x in input().split()] # list comprehension
is_even = lambda x: x % 2 == 0 # == True
result = list(filter(is_even, numbers_as_digits))
print(result)

# filter(function, iterable_object)
# function - там стои функцията
# iterable_object - това трябва да е list, set или tuple
