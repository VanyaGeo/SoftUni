# import re
#
# text = input()
# pattern = r"(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
#
# matches = re.finditer(pattern, text)
# for match in matches:
#     day = match.group(1) # == group("day")
#     month = match.group(3) # == group("month")
#     year = match.group(4) # == group("year")
#
#     print(f"Day: {day}, Month: {month}, Year: {year}")


# II

import re

text = input()
pattern = r"(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"

matches = re.finditer(pattern, text)
for match in matches:
    print(f"Day: {match[1]}, Month: {match[3]}, Year: {match[4]}")

# 13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016