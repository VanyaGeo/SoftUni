lines = int(input())
total_sum = 0

for line in range(1, lines +1 ):
    ascii_character = input()
    ascii_number = ord(ascii_character)
    total_sum = total_sum + ascii_number
print(f"The sum equals: {total_sum}")


# ord(...) -> to input a number from the ASCII table
# chr(...) -> to input a character from the ASCII table
