# I
#
# def add_and_subtract(first, second, third):
#     def sum_numbers(first1, second1):
#         sum_of_number = first1 + second1
#         return sum_of_number
#
#     def subtract(sum_num, third1):
#         subtract_of_numbers = sum_num - third1
#         return subtract_of_numbers
#     sum_of_first_and_second = sum_numbers(first, second)
#     result = subtract(sum_of_first_and_second, third)
#     return result
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
# final_result = add_and_subtract(first_number, second_number, third_number)
# print(final_result)


# II

def sum_numbers(first, second):
    return first + second


def subtract(sum_num, third):
    return sum_num - third


def add_and_subtract(first, second, third):
    sum_of_first_and_second = sum_numbers(first, second)
    subtract_of_numbers = subtract(sum_of_first_and_second, third)
    return subtract_of_numbers


first_number = int(input())
second_number = int(input())
third_number = int(input())

final_result = add_and_subtract(first_number, second_number, third_number)
print(final_result)
