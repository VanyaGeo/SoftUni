first_string_list = input().split(", ")
second_string_list = input().split(", ")

new_list = []

for word in first_string_list:
    for word_ in second_string_list:
        if word in word_ and not word in new_list:
            new_list.append(word)

print(new_list)