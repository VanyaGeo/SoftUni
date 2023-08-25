key_word = input()
random_string = input()

while key_word in random_string:
    random_string = random_string.replace(key_word, "")

print(random_string)

# ice
# kicegiciceeb