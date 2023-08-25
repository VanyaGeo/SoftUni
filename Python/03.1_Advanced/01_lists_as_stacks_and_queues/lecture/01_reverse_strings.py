# I
# text = [char for char in input()]
#
# reversed_text = []
#
# for symbol in range(len(text)):
#     reversed_text.append(text.pop())
#
# print("".join(reversed_text))

# II

# text = list(input())
#
# while text:
#     reversed_element = text.pop()
#     print(reversed_element, end="")

# III

text = [char for char in input()]
text.reverse()
print("".join(text))