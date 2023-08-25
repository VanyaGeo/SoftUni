count = int(input())
synonyms = {}

for i in range(count):
    key = input()
    value = input()

    if key not in synonyms:
        synonyms[key] = []
    synonyms[key].append(value)

for word, word_synonyms in synonyms.items():
    print(f"{word} - {', '.join(word_synonyms)}")
