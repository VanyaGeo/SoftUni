user_input = input()

digits = ""
letters = ""
symbols = ""

for char in user_input:
    if char.isdigit():
        digits += str(char)
    elif char.isalpha():
        letters += char
    else:
        symbols += char

print(digits)
print(letters)
print(symbols)

# Agd#53Dfg^&4F53