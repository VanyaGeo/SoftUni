text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

text_with_no_vowels = [letter for letter in text if letter not in vowels]

print("".join(text_with_no_vowels))


# text_with_no_vowels = []
#
# for letter in text:
#     if letter not in vowels:
#         text_with_no_vowels.append(letter)
#
# result = "".join(text_with_no_vowels)
# print(result)