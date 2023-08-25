import re

sentence = input()
key_word = input()
pattern = fr"\b{key_word}\b"

matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
print(len(matches))


# How do you plan on achieving that? How? How can you even think of that?
# how