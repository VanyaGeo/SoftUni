user_licence_dict = {}

number_of_commands = int(input())

for number in range(number_of_commands):
    arguments = input().split()
    command = arguments[0]
    username = arguments[1]

    if command == "register":
        license_plate = arguments[2]
        if username in user_licence_dict:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            user_licence_dict[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif command == "unregister":
        if username in user_licence_dict:
            user_licence_dict.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for key, value in user_licence_dict.items():
    print(f"{key} => {value}")


# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy
