# import re
#
# sentence = input()
# pattern = r"\d+"
# result = []
#
# while sentence:
#     matches = re.findall(pattern, sentence)
#     result.extend(matches)
#     sentence = input()
#
# print(" ".join(result))
#

# II

import re

sentence = input()
pattern = r"\d+"

while sentence:
    matches = re.findall(pattern, sentence)
    if matches:
        print(" ".join(matches), end=" ")
    sentence = input()

# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45
