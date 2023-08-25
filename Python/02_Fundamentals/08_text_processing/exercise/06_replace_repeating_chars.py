sequence_of_letters = input()
result = sequence_of_letters[0]

for letter in sequence_of_letters:
    if letter != result[-1]:
        result += letter

print(result)

# aaaaabbbbbcdddeeeedssaa