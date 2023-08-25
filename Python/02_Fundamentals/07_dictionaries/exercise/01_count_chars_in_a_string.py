letters_dict = {}

words_input = "".join(word for word in input().split())

for letter in words_input:
    if letter not in letters_dict:  # == if letter not in letters_dict.keys():
        letters_dict[letter] = 0
    letters_dict[letter] += 1

for letter, amount in letters_dict.items():
    print(f"{letter} -> {amount}")

# for letter in letters_dict.keys():
#     print(f"{letter} -> {letters_dict[letter]}")
# това е още едни вариант

# text text text