import re

text = input()

pattern = r"([@#]+)([a-z]{3,})([@#]+)([^A-Za-z\d]*)\/+(\d+)\/"

#  (@|#)+(?P<color>[a-z]{3,})(@|#)+[^A-Za-z0-9]+/+(?P<amount>\d+)/+

matches = re.findall(pattern, text)
valid_eggs = []
for match in matches:
    color = match[1]
    amount = match[4]
    valid_eggs.append(f"You found {amount} {color} eggs!")

if valid_eggs:
    print("\n".join(valid_eggs))
