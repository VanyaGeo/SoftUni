list_of_phones = input().split(", ")

command_ = input()

while command_ != "End":
    command = command_.split()
    if command[0] == "Add":
        if not command[2] in list_of_phones:
            list_of_phones.append(command[2])

    elif command[0] == "Remove":
        if command[2] in list_of_phones:
            list_of_phones.remove(command[2])

    elif command[0] == "Bonus":
        to_do = command[3].split(":")
        old_phone = to_do[0]
        new_phone = to_do[1]
        if old_phone in list_of_phones:
            indx = list_of_phones.index(old_phone)
            list_of_phones.insert(indx+1, new_phone)

    elif command[0] == "Last":
        if command[2] in list_of_phones:
            list_of_phones.remove(command[2])
            list_of_phones.append(command[2])

    command_ = input()

if command_ == "End":
    print(", ".join(list_of_phones))

