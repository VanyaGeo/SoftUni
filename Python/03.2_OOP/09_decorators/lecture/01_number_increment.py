# def number_increment(numbers):
#     def increase():
#         increased_numbers = []
#         for number in numbers:
#             increased_numbers.append(number + 1)
#         return increased_numbers
#     return increase()


def number_increment(numbers):
    def increase():
        return [number + 1 for number in numbers]
    return increase()


print(number_increment([1, 2, 3]))