number_of_commands = int(input())
parking = set()

for command in range(number_of_commands):
    direction, car_number = input().split(", ")
    if direction == "IN":
        parking.add(car_number)
    elif direction == "OUT":
        parking.remove(car_number)


if len(parking) > 0:
    print("\n".join(parking))
else:
    print("Parking Lot is Empty")
