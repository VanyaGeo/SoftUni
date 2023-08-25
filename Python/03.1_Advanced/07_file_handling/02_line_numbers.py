# from string import punctuation
# # punctuation = ["-", ",", ".", "!", "?"]
#
# with open("text.txt", "r") as file:
#     text = file.readlines()
#
# with open("output.txt", "w") as result_file:
#
#     for line in range(len(text)):
#         letters = 0
#         symbols = 0
#
#         for character in text[line]:
#             if character.isalpha():
#                 letters += 1
#             elif character in punctuation:
#                 symbols += 1
#             else:  # => if character.isspace():
#                 continue
#
#         result_file.write(f"Line {line + 1}: {text[line].strip()} ({letters})({symbols})\n")
#
# result_file.close()
#

import os

root_path = os.path.dirname(__file__)
rows = 3
count_lines = 1

with open(os.path.join(root_path, "temporary_text.txt"), "a") as text_file:
    print("Enter 3 sentences from README.txt on the next line:")
    for row in range(rows):
        text_file.write(input() + "\n")

with open(os.path.join(root_path, "temporary_text.txt"), "r") as text_file_lines:
    lines = text_file_lines.readlines()

with open(os.path.join(root_path, "output.txt"), "a") as output_file:
    for line in lines:

        count_symbols = 0
        count_letter = 0

        line = line.strip("\n")

        for char in line:
            if char.isalpha():
                count_letter += 1
            elif not char.isalpha() and char != " ":
                count_symbols += 1

        output_file.write(f"Line {count_lines}: {line} ({count_letter})({count_symbols})" + "\n")
        count_lines += 1

with open("output.txt", "r") as output:
    print(output.read())

# Note: After printing output.txt it's going to be erased!
os.remove("output.txt")
os.remove("temporary_text.txt")
