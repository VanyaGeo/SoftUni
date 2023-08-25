# import re
#
# text = input()
# pattern = r"(^|(?<=\s))-?([1-9][0-9]*|[0])(.[0-9]+)?($|(?=\s))"
# list_of_numbers = []
# matches = re.finditer(pattern, text)
#
# for match in matches:
#     list_of_numbers.append(match.group())
#
# print(" ".join(list_of_numbers))

# II
#
# import re
#
# text = input()
# pattern = r"(^|(?<=\s))-?([1-9][0-9]*|[0])(.[0-9]+)?($|(?=\s))"
# matches = re.finditer(pattern, text)
#
# for match in matches:
#     print(match.group(), end=" ")

# III

import re

text = input()
pattern = r"((^|(?<=\s))-?([1-9][0-9]*|[0])(.[0-9]+)?($|(?=\s)))"
matches = re.finditer(pattern, text)

for match in matches:
    print(match[0], end=" ")


# 1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5 00.5