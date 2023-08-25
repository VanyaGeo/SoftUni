pirate_ship_status = [int(x) for x in input().split(">")]
warship_status = [int(x) for x in input().split(">")]
max_health_capacity = int(input())

commands = input()

stalemate = True

while commands != "Retire":
    if stalemate is False:
        break
    command = commands.split()
    if command[0] == "Fire":
        indx = int(command[1])
        damage = int(command[2])
        if 0 <= indx < len(warship_status):
            warship_status[indx] -= damage
            if warship_status[indx] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        for indexes in range(start_index, end_index + 1):
            if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
                pirate_ship_status[indexes] -= damage
                if pirate_ship_status[indexes] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
            else:
                break
    elif command[0] == "Repair":
        indx = int(command[1])
        health = int(command[2])
        if 0 <= indx < len(pirate_ship_status):
            pirate_ship_status[indx] += health
            if pirate_ship_status[indx] > max_health_capacity:
                pirate_ship_status[indx] = max_health_capacity
    elif command[0] == "Status":
        count_section = 0
        for section in pirate_ship_status:
            if section < max_health_capacity * 0.2:
                count_section += 1
        print(f"{count_section} sections need repair.")
    commands = input()

if stalemate is True:
    print(f"""Pirate ship status: {sum(pirate_ship_status)}
Warship status: {sum(warship_status)}""")
