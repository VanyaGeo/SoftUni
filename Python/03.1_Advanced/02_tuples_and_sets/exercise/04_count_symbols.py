text = input()

occurrences = {}

for letter in text:
    # if letter not in occurrences:
    #     occurrences[letter] = 0
    # occurrences[letter] += 1
    occurrences[letter] = occurrences.get(letter, 0) + 1

for letter, number in sorted(occurrences.items()):
    print(f"{letter}: {number} time/s")

# II
#
# text = input()
#
# for letter in sorted(set(text)):
#     print(f"{letter}: {text.count(letter)} time/s")
