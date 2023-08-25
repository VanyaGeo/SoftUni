def vowel_filter(function):
    # vowels = ["a", "e", "i", "o", "u"] - може да е тук, може и да е долу
    def wrapper():
        vowels = ["a", "e", "i", "o", "u"]
        return [letter for letter in function() if letter in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())
