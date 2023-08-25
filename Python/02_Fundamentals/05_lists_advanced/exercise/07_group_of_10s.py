list_of_numbers = [int(x) for x in input().split(", ")]  #8, 12, 38, 3, 17, 19, 25, 35, 50

group = 10

while list_of_numbers:
    new_list = []
    for number in list_of_numbers:
        if number in range(group - 10, group + 1):
            new_list.append(number)
    for number in new_list:
        list_of_numbers.remove(number)
    print(f"Group of {group}'s: {new_list}")
    group += 10
