number_of_cars = int(input())
car_dict = {}

for i in range(number_of_cars):
    car_args = input().split("|")
    car = car_args[0]
    mileage = int(car_args[1])
    fuel = int(car_args[2])
    car_dict[car] = {"mileage": mileage, "fuel": fuel}

line = input()

while line != "Stop":
    instructions = line.split(" : ")
    command = instructions[0]

    if command == "Drive":
        car_info = instructions[1]
        distance_info = int(instructions[2])
        fuel_info = int(instructions[3])
        if car_dict[car_info]["fuel"] < fuel_info:
            print("Not enough fuel to make that ride")
        else:
            car_dict[car_info]["mileage"] += distance_info
            car_dict[car_info]["fuel"] -= fuel_info
            print(f"{car_info} driven for {distance_info} kilometers. {fuel_info} liters of fuel consumed.")
        if car_dict[car_info]["mileage"] >= 100000:
            del car_dict[car_info]
            print(f"Time to sell the {car_info}!")

    elif command == "Refuel":
        car_info = instructions[1]
        fuel_info = int(instructions[2])
        current_fuel = car_dict[car_info]["fuel"]
        car_dict[car_info]["fuel"] += fuel_info
        if car_dict[car_info]["fuel"] > 75:
            car_dict[car_info]["fuel"] = 75
        consumed_fuel = car_dict[car_info]["fuel"] - current_fuel
        print(f"{car_info} refueled with {consumed_fuel} liters")

    elif command == "Revert":
        car_info = instructions[1]
        kilometers = int(instructions[2])
        car_dict[car_info]["mileage"] -= kilometers
        if car_dict[car_info]["mileage"] >= 10000:
            print(f"{car_info} mileage decreased by {kilometers} kilometers")
        else:
            car_dict[car_info]["mileage"] = 10000

    line = input()

for key, value in car_dict.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")

# 4
# Lamborghini Veneno|11111|74
# Bugatti Veyron|12345|67
# Koenigsegg CCXR|67890|12
# Aston Martin Valkryie|99900|50
# Drive : Koenigsegg CCXR : 382 : 82
# Drive : Aston Martin Valkryie : 99 : 23
# Drive : Aston Martin Valkryie : 2 : 1
# Refuel : Lamborghini Veneno : 40
# Revert : Bugatti Veyron : 2000
# Stop