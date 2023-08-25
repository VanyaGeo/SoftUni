floor_amount = int(input())
room_amount_per_floor = int(input())

result_for_last_floor = ""
for last_floor_room in range(room_amount_per_floor):
    curr_room = f"L{floor_amount}{last_floor_room}"
    result_for_last_floor += f" {curr_room}"

print(result_for_last_floor)

for current_floor in range(floor_amount-1, 0, -1):
    result = ""
    for current_room in range(room_amount_per_floor):
        if current_floor % 2 == 0:
            room = f"O{current_floor}{current_room}"
            result += f" {room}"

        elif current_floor % 2 == 1:
            room = f"A{current_floor}{current_room}"
            result += f" {room}"

    print(result)
