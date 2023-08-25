import re

line = input()
pattern = r"\b_([A-Za-z0-9]+)\b" # в този случай скобите подсказват да се принтира само намереното в тях (без "_")

result = re.findall(pattern, line)

print(",".join(result))


# __invalidVariable _evenMoreInvalidVariable_ _validVariable