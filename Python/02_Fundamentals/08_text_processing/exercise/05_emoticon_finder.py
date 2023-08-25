text = input()
emoticon = ""

for index in range(len(text)):
    char = text[index]
    if char == ":":
        emoticon = char + text[index+1]
        print(emoticon)


# There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)