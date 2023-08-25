I
# command = input()
#
# while command != "End":
#     output = ""
#     if command != "SoftUni":
#         for letters in command:
#             output = output + letters * 2
#         print(output)
#     command = input()

II
# command = input()
#
# while command != "End":
#     if command == "SoftUni":
#         pass
#     else:
#         text = ""
#         for i in command:
#             text += (i * 2)
#         print(text)
#     command = input()


III
while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    for letters in command:
        print(f"{letters}{letters}", end="")

    print()