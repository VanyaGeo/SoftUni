def func_executor(*args):
    # return '\n'.join([f"{func.__name__} - {func(*arguments)}" for func, arguments in args])
    result = []
    for func, arguments in args:
        func_name = func.__name__
        func_result = func(*arguments)
        result.append(f"{func_name} - {func_result}")
    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
