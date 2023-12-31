def logged(func):
    def wrapper(*args):
        return f"you called {func.__name__}" \
               f"{args}\n" \
               f"it returned {func(*args)}"

# ред 4 може и така =>   f"({', '.join(str(arg) for arg in args)})\n" \

    return wrapper


@logged
def func(*args):
    return 3 + len(args)

print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b

print(sum_func(1, 4))



# import unittest
#
# class LoggedTests(unittest.TestCase):
#     def test_zero(self):
#         @logged
#         def func(*args):
#             return 3 + len(args)
#         result = func(4, 4, 4)
#         self.assertEqual(result, 'you called func(4, 4, 4)\nit returned 6')
#
# if __name__ == '__main__':
#     unittest.main()