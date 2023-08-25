def rectangle(length, width):

    if not isinstance(length, int) or not isinstance(width, int):
        return f"Enter valid values!"

    def area():
        return width * length

    def perimeter():
        return 2 * length + 2 * width

    return f"Rectangle area: {area()}\n" \
           f"Rectangle perimeter: {perimeter()}"


print(rectangle(2, 10))

print(rectangle('2', 10))
