import re

text = input()
pattern = r"(@|#)([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)"
matches = re.findall(pattern, text)

list_of_mirror_matches = []
valid_pairs = 0

for match in matches:
    if match[1] == match[4][::-1]:
        list_of_mirror_matches.append(f"{match[1]} <=> {match[4]}")
    valid_pairs += 1

if valid_pairs == 0:
    print("No word pairs found!")
elif valid_pairs > 0:
    print(f"{valid_pairs} word pairs found!")
if len(list_of_mirror_matches) == 0:
    print("No mirror words!")
elif len(list_of_mirror_matches) > 0:
    print(f"The mirror words are:\n{', '.join(list_of_mirror_matches)}")


# @mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r