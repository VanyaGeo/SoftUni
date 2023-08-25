# import re
#
# line = input()
# pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"
# match = re.findall(pattern, line)
#
# print(", ".join(match))

# +359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222

# II

import re

line = input()
pattern = r"\+359([ -])2\1\d{3}\1\d{4}\b"
# в този случай създавам група ([ -]) след това \1 означава че на това място искам да използвам елемент от тази първа група
matches = re.finditer(pattern, line)

output = []
for match in matches:
    output.append(match.group())

print(", ".join(output))