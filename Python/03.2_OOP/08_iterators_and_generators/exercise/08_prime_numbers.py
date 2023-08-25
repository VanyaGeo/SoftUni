from math import sqrt
# импортваме корен квадратен

def get_primes(numbers: list):
    for num in numbers:
        if num <= 1:  # ако числото е по-малко или равно на 1, значи не е прайм
            continue

        for divisor in range(2, int(sqrt(num)) + 1):  # числата от 2 до половината на на нашето чсило включително
            if num % divisor == 0:  # ако можем да извършим деление без остатък (4 : 2 = 2, остатък 0)
                break

        else:  # ако не брейкнем цикъла, числото е прайм и го извикваме
            yield num


# II без импортване на корен квадратен от мат:

# def get_primes(numbers: list):
#     for num in numbers:
#         if num <= 1:  # ако числото е по-малко или равно на 1, значи не е прайм
#             continue
#
#         for divisor in range(2, int(num ** 0.5) + 1):  # числата от 2 до половината на нашето чсило включително
#             if num % divisor == 0:  # ако можем да извършим деление без остатък (4 : 2 = 2, остатък 0)
#                 break
#
#         else:  # ако не брейкнем цикъла, числото е прайм и го извикваме
#             yield num


# III не е оптимално решение: (отнема много време и памет)

# def get_primes(numbers: list):
#     for number in numbers:
#         if number <= 1:  # ако числото е по-малко или равно на 1, значи не е прайм
#             continue
#
#         for divisor in range(2, number):  # числата от 2 до нашето число ексклузивно
#             if number % divisor == 0:  # ако можем да извършим деление без остатък (4 : 2 = 2, остатък 0)
#                 break
#
#         else:  # ако не брейкнем цикъла, числото е прайм и го извикваме
#             yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
