from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

keywords = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}

found_word = ""

while vowels and consonants:

    cur_vow = vowels.popleft()
    cur_cons = consonants.pop()
    for word, value in keywords.items():
        if cur_vow in keywords[word]:
            keywords[word] = keywords[word].replace(cur_vow, "")
        if cur_cons in keywords[word]:
            keywords[word] = keywords[word].replace(cur_cons, "")
        if keywords[word] == "":
            found_word = word
            break
    if found_word:
        break

if found_word:
    print(f"Word found: {found_word}")
if not found_word:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(v for v in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(c for c in consonants)}")


