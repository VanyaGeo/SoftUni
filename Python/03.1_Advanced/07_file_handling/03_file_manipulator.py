import os

command = input()

while command != 'End':
    command = command.split('-')

    if command[0] == "Create":
        file = open(command[1], "w")
        file.close()

    elif command[0] == "Add":
        with open(command[1], "a") as file:
            file.write(f"{command[2]}\n")

    elif command[0] == "Replace":
        try:
            with open(command[1], "r+") as file:
                text = file.read()
                text = text.replace(command[2], command[3])
                file.seek(0)  # - връща курсора в началото на файла, за да се направят промените
                file.write(text)

        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == "Delete":
        try:
            os.remove(command[1])
        except FileNotFoundError:
            print("An error occurred")

    command = input()


# import os
# print("Enter text from README.txt on the next line:")
#
# root_path = os.path.dirname(__file__)
#
# while True:
#     command = input()
#     if command == "End":
#         break
#
#     command = command.split("-")
#     file_name = command[1]
#
#     file_path = os.path.join(root_path, file_name)
#
#     if command[0] == "Create":
#         file = open(file_path, 'w')
#         file.write("")
#
#     elif command[0] == "Add":
#         content = command[2]
#         file = open(file_path, 'a')
#         file.write(content + "\n")
#
#     elif command[0] == "Replace":
#         old_string = command[2]
#         new_string = command[3]
#         try:
#             file = open(file_path, 'r+')
#             text = file.read()
#             text = text.replace(old_string, new_string)
#             file.seek(0)
#             file.write(text)
#
#         except FileNotFoundError:
#             print("An error occurred")
#
#     elif command[0] == "Delete":
#         try:
#             os.remove(file_name)
#         except FileNotFoundError:
#             print("An error occurred")
#
#     file.close()

