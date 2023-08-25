list_numbers = input().split(" ")
list_opposite_numbers = []

for elements in list_numbers:
    number = -int(elements)
    list_opposite_numbers.append(number)

print(list_opposite_numbers)

# входни данни: -4 0 2 57 -101