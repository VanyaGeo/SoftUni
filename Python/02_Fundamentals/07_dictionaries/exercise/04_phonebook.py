command = input()

phone_book_dict = {}

while "-" in command:
    name, number = command.split("-")
    phone_book_dict[name] = number
    command = input()

number_of_searched_people = int(command)
for people in range(number_of_searched_people):
    searched_people = input()
    if searched_people in phone_book_dict:
        print(f"{searched_people} -> {phone_book_dict[searched_people]}")
    else:
        print(f"Contact {searched_people} does not exist.")


# Adam-+359888001122
# Ralf-666
# George-5559393
# Silvester-02/987665544
# 4
# Silvester
# silvester
# Rolf
# Ralf
