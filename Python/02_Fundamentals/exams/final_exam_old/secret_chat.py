message = input()
command_to_do = input()

while command_to_do != "Reveal":
    instructions = command_to_do.split(":|:")
    command = instructions[0]
    if command == "InsertSpace":
        index = int(instructions[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif command == "Reverse":
        substring = instructions[1]
        if substring in message:
            message = message.replace(substring, "", 1) + substring[::-1]
            print(message)
        else:
            print("error")
    elif command == "ChangeAll":
        substring = instructions[1]
        replacement = instructions[2]
        message = message.replace(substring, replacement)
        print(message)

    command_to_do = input()

print(f"You have a new text message: {message}")


# Hiware?uiy
# ChangeAll:|:i:|:o
# Reverse:|:?uoy
# Reverse:|:jd
# InsertSpace:|:3
# InsertSpace:|:7
# Reveal