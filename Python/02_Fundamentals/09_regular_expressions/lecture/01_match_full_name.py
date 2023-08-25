import re

sentence = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

match = re.findall(pattern, sentence)

print(" ".join(match))


# Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett

