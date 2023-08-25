number = int(input())
key_word = input()

list_of_strings = []

for line in range(number):
    string = input()
    list_of_strings.append(string)
print(list_of_strings)
for index in range(len(list_of_strings)-1, -1, -1):
    index_string = list_of_strings[index]
    if key_word not in index_string:
        list_of_strings.remove(index_string)
print(list_of_strings)

