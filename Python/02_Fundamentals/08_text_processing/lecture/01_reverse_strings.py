# word = input()
#
# while word != "end":
#     reversed_word = ""
#     for letters in word[::-1]:
#         reversed_word += letters
#     print(f"{word} = {reversed_word}")
#     word = input()

# [::-1] това е същото като [-1:0:-]

# II

word = input()

while word != "end":
    print(f"{word} = {word[::-1]}")
    word = input()

# III

word = input()

while word != "end":
    reversed_word = ""
    for letters in reversed(word):
        reversed_word += letters
    print(word + "=" + reversed_word)
    word = input()


# helLo
# Softuni
# bottle
# end
