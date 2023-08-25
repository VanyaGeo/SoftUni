def even_odd(*args):

    def even():
        return [x for x in args[:-1] if x % 2 == 0]

    def odd():
        return [x for x in args[:-1] if x % 2 == 1]

    if args[-1] == "even":
        return even()

    else:
        return odd()


print(even_odd(1, 2, 3, 4, 5, 6, "even"))

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))