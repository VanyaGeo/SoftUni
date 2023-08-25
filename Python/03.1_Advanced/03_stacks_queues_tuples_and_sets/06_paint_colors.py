from collections import deque

text = deque(input().split())  # d yel blu e low redd

colors = {"red", "yellow", "blue", "orange", "purple", "green"}
mixed_colors = {
    "orange": {"yellow", "red"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

result = []

while text:
    first_word = text.popleft()
    if len(text) > 0:
        second_word = text.pop()
    else:
        second_word = ""

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first_word[:-1], second_word[:-1]):
            if el:
                text.insert(len(text) // 2, el)

for color in set(mixed_colors.keys()).intersection(result): # iterate over every secondary color that we have
    if not mixed_colors[color].issubset(result):  # check if we have the needed colors to have the secondary color
        result.remove(color)

print(result)