def between_characters(first, second):
    for chars in range(ord(first_character) + 1, ord(second_character)):
        list_of_characters.append(chr(chars))
    return list_of_characters


first_character = input()
second_character = input()
list_of_characters = []
result = between_characters(first_character, second_character)
final_result = " ".join(result)
print(final_result)