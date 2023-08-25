list_of_words = [word for word in input().split(" ") if len(word) % 2 == 0]

print(*list_of_words, sep="\n")

# ==> print list оn new lines without a separator