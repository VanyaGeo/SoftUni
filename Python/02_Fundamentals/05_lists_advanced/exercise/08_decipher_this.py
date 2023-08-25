secret_message = input().split(" ")

final_message = []
current_message = ''

for ciphered_word in secret_message:
    digits = ''

    for ciphered_elements in ciphered_word:
        if ciphered_elements.isdigit():
            digits += ciphered_elements

    current_message = chr(int(digits))
    ciphered_word = ciphered_word.replace(digits, current_message)

    if len(ciphered_word) > 2:
        ciphered_word = ciphered_word[0] + ciphered_word[-1] + ciphered_word[2:-1] + ciphered_word [1]
    final_message.append(ciphered_word)

result = " ".join(final_message)
print(result)


    # ciphered_word[0], ciphered_word[-1] = ciphered_word[-1], ciphered_word[0] # това би работило само за листове

    # ciphered_word = ciphered_word[0] + ciphered_word[-1] + ciphered_word[2:-1] + ciphered_word [1]
# това работи за елементи в стрингове ^