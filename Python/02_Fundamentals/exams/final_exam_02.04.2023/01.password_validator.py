import re

password = input()
commands = input()

while commands != "Complete":
    instructions = commands.split()
    command = instructions[0]
    if command == "Make":
        key_command = instructions[1]
        if key_command == "Upper":
            indx = int(instructions[2])
            password = password[:indx] + password[indx].upper() + password[indx + 1:]
            print(password)

        elif key_command == "Lower":
            indx = int(instructions[2])
            password = password[:indx] + password[indx].lower() + password[indx + 1:]
            print(password)

    elif command == "Insert":
        indx = int(instructions[1])
        char = instructions[2]
        if -len(password) <= indx < len(password):
            password = password[:indx] + char + password[indx:]
            print(password)

    elif command == "Replace":
        char = instructions[1]
        value = int(instructions[2])
        ascii_value = chr(ord(char) + value)
        if char in password:
            password = password.replace(char, ascii_value)
            print(password)

    elif command == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        if not(re.match(r'^\w+$', password)):
            print("Password must consist only of letters, digits and _!")
        if not(any(c.isupper() for c in password)):
            print("Password must consist at least one uppercase letter!")
        if not(any(c.islower() for c in password)):
            print("Password must consist at least one lowercase letter!")
        if not(any(c.isdigit() for c in password)):
            print("Password must consist at least one digit!")

    commands = input()
