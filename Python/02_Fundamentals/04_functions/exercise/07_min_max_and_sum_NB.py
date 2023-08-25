def min_max_sum_of_numbers(nums):
    min_number = 0
    max_number = 0
    sum_of_numbers = 0
    for number in nums:
        min_number = min(nums)
        max_number = max(nums)
        sum_of_numbers = sum(nums)
    return min_number, max_number, sum_of_numbers


numbers_as_digits = [int(x) for x in input().split()]
min_num, max_num, sum_num = min_max_sum_of_numbers(numbers_as_digits)
print(f"""The minimum number is {min_num} 
The maximum number is {max_num} 
The sum number is: {sum_num}""")

# NB! този формат на print с три кавички в началото и в края позволяват принтиране на няколко реда!!