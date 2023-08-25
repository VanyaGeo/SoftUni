list_nums = [int(x) for x in input().split()]

command_ = input()

while command_ != "Finish":
    command = command_.split()
    value = int(command[1])

    if command[0] == "Add":
        list_nums.append(value)

    elif command[0] == "Remove":
        if value in list_nums:
            list_nums.remove(value)

    elif command[0] == "Replace":
        replacement = int(command[2])
        if value in list_nums:
            indx = list_nums.index(value)
            list_nums[indx] = replacement

    elif command[0] == "Collapse":
        list_nums = [num for num in list_nums if num >= value]

    command_ = input()

if command_ == "Finish":
    result = [str(num) for num in list_nums]
    print(" ".join(result))
