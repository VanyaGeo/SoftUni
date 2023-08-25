from functools import reduce


def operate(operator, *args):

    result = reduce(lambda a, b: eval(f"{a}{operator}{b}"), args)
    return result


print(operate("-", 3, 6))


# II

# from functools import reduce
#
#
# def operate(operator, *args):
#
#     if operator == "+":
#         return reduce(lambda a, b: a + b, args)
#     elif operator == "-":
#         return reduce(lambda a, b: a - b, args)
#     elif operator == "*":
#         return reduce(lambda a, b: a * b, args)
#     elif operator == "/":
#         return reduce(lambda a, b: a / b, args)
#
#
# print(operate("+", 1, 2, 3))

# III
#
#
# def operate(*args):
#
#     def sum_nums():
#         return sum(args[1:])
#
#     def subtract_nums():
#         result = args[1]
#         for num in args[2:]:
#             result -= num
#         return result
#
#     def multiply_nums():
#         result = args[1]
#         for num in args[2:]:
#             result *= num
#         return result
#
#     def divide_nums():
#         result = args[1]
#         for num in args[2:]:
#             result /= num
#         return result
#
#     if args[0] == "+":
#         return sum_nums()
#     elif args[0] == "-":
#         return subtract_nums()
#     elif args[0] == "*":
#         return multiply_nums()
#     elif args[0] == "/":
#         return divide_nums()
#
#
# print(operate("+", 1, 2, 3))