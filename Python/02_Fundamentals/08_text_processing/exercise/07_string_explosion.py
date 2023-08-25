text = input()
final = ""
explosion = 0

for i in range(len(text)):
    if text[i] == ">":
        explosion += int(text[i + 1])
        final += text[i]
        continue
    elif explosion > 0:
        explosion -= 1
        continue
    final += text[i]

print(final)


# II

# text = input()
# new_text = list()
# strength = 0
#
# for ch in text:
#     if ch.isdigit():
#         strength += int(ch)
#         strength -= 1
#     else:
#         if strength < 1:
#             new_text.append(ch)
#         else:
#             if ch == ">":
#                 new_text.append(ch)
#             else:
#                 strength -= 1
#
# print("".join(new_text))

# abv>1>1>2>2asdasd