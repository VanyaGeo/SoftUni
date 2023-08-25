from collections import deque

water_quantity = int(input())
name_ppl = input()

que_of_people = deque()

while name_ppl != "Start":
    que_of_people.append(name_ppl)
    name_ppl = input()

command_ = input()

while command_ != "End":
    command = command_.split()

    if command[0] == "refill":
        water_quantity += int(command[1])
    else:
        if int(command[0]) <= water_quantity:
            print(f"{que_of_people.popleft()} got water")
            water_quantity -= int(command[0])
        else:
            print(f"{que_of_people.popleft()} must wait")

    command_ = input()

# if command_ == "End":
else:
    print(f"{water_quantity} liters left")
