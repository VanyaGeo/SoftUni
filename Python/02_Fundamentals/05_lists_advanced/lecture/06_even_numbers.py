numbers = input().split(", ")

# even_numbers = [int(number) for number in numbers if int(number) % 2 == 0]
index_even_number = [index for index in range(len(numbers)) if int(numbers[index]) % 2 == 0]

# print(even_numbers)
print(index_even_number)



