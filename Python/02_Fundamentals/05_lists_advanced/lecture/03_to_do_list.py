command = input()
to_do_list = [0] * 11

while command != "End":
    number, task = command.split("-")
    index = int(number) # -1
    to_do_list[index] = task
    command = input()


print([elements for elements in to_do_list if elements != 0])
