# # import os
# #
# # current_directory = os.path.dirname(os.path.abspath(__file__))
# # file_path = os.path.join(current_directory, "text.txt")
#
# symbols = ["-", ",", ".", "!", "?"]
#
# with open("text.txt", "r") as file:  # - може вместо "text.txt" да се използва file_path с горните редове
#     text = file.readlines()
#
# for row_index in range(len(text)):
#     if row_index % 2 == 0:
#         for char in symbols:
#             text[row_index] = text[row_index].replace(char, "@")
#
#         result = ' '.join(text[row_index].split()[::-1])
#         print(result)

import os
from collections import deque

root_path = os.path.dirname(__file__)

rows = 3
symbols = {"-", ",", ".", "!", "?"}

with open(os.path.join("temporary_text.txt"), "a") as text_file:
    print("Enter 3 sentences from README.txt on the next line:")
    for row in range(rows):
        text_file.write(input() + "\n")

with open("temporary_text.txt", "r") as sentences_file:
    sentences_file_list = sentences_file.readlines()

for i in range(len(sentences_file_list)):
    sentences_file_list[i] = sentences_file_list[i].strip("\n")
    sentence = deque()

    if i % 2 == 0:
        for symbol in symbols:
            sentences_file_list[i] = sentences_file_list[i].replace(symbol, "@")

        sentence.extend(sentences_file_list[i].split())

        for _ in range(len(sentence)):
            print(sentence.pop(), end=" ")
        print()

os.remove("temporary_text.txt")

