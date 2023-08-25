def sum_even_and_odd(num):
    sum_of_even = 0
    sum_of_odd = 0
    for digit in num:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        elif int(digit) % 2 == 1:
            sum_of_odd += int(digit)
    return sum_of_even, sum_of_odd


number = input()
sum_of_even, sum_of_odd = sum_even_and_odd(number)
print(f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}")

