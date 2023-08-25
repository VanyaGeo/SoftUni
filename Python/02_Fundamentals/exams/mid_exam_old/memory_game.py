def is_index_in_range(index, list):
    if 0 <= index < list:
        return True
    return False


def is_index_valid(index_1, index_2, list):
    if is_index_in_range(index_1, list) and is_index_in_range(index_2, list) and index_1 != index_2:
        return True
    return False


card_list = input().split()

command = input()

number_of_moves = 0

while command != "end":
    command_indexes = [int(x) for x in command.split()]
    indx_1, indx_2 = command_indexes

    number_of_moves += 1

    if not is_index_valid(indx_1, indx_2, len(card_list)):
        element = f"-{number_of_moves}a"
        middle_of_list = len(card_list) // 2
        card_list.insert(middle_of_list, element)
        card_list.insert(middle_of_list, element)
        print("Invalid input! Adding additional elements to the board")
    else:
        if card_list[indx_1] == card_list[indx_2]:
            element = card_list[indx_1]
            card_list.remove(element)
            card_list.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        elif card_list[indx_1] != card_list[indx_2]:
            print("Try again!")

    if len(card_list) == 0:
        print(f"You have won in {number_of_moves} turns!")
        exit()

    command = input()


print(f"""Sorry you lose :(
{" ".join(card_list)}""")
