# рекурсия е функция, която извиква сама себе си
# пример:
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(5))

# output: 120 (защото умножаваме 5 * 4 * 3 * 2 * 1 във факториал-а)


def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))


# всичко това може да се запише само с един ред: print(2 ** 10)
