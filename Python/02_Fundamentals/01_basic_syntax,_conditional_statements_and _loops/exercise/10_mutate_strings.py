# сложна задача!!!

string_1 = input()
string_2 = input()
last_printed_string = string_1

for letter_index in range(len(string_1)):
    left_part = string_2[0:letter_index+1:1]  # ==> [:letter_index+1]
    right_part = string_1[letter_index+1:len(string_1):1]  # ==> [letter_index+1:]
    current_string = left_part + right_part
    if current_string == last_printed_string:
        continue
    print(current_string)
    last_printed_string = current_string

