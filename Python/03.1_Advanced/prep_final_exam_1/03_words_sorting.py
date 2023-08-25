def words_sorting(*args):
    word_dict = {}
    sorted_dict = {}
    result = ""
    for word in args:
        word_dict[word] = 0
        for letter in word:
            word_dict[word] += ord(letter)
    total_sum_dict = sum(word_dict.values())
    if total_sum_dict % 2 == 0:
        sorted_dict = sorted(word_dict.items(), key=lambda x: x[0])
    else:
        sorted_dict = sorted(word_dict.items(), key=lambda x: -x[1])
    for key, value in sorted_dict:
        result += f"{key} - {value}\n"
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))