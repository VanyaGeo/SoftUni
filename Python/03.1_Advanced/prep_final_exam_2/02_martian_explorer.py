rows = 6
matrix = []
rover_position = []

for row in range(rows):
    matrix.append(input().split())
    if "E" in matrix[row]:
        rover_position = [row, matrix[row].index("E")]

commands = input().split(", ")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

found_deposits = {
    "W": 0,  # Water deposit
    "M": 0,  # Metal deposit
    "C": 0   # Concrete deposit
}
row = rover_position[0]
column = rover_position[1]

for command in commands:
    new_row = directions[command][0]
    new_column = directions[command][1]

    row += new_row
    column += new_column

    if row > 5:
        row = 0
    if row < 0:
        row = 5
    if column > 5:
        column = 0
    if column < 0:
        column = 5

    if matrix[row][column] == "R":
        print(f"Rover got broken at ({row}, {column})")
        break

    elif matrix[row][column] in found_deposits:
        found_deposits[matrix[row][column]] += 1
        deposit_name = ""
        if matrix[row][column] == "W":
            deposit_name = "Water"
        elif matrix[row][column] == "M":
            deposit_name = "Metal"
        elif matrix[row][column] == "C":
            deposit_name = "Concrete"
        print(f"{deposit_name} deposit found at ({row}, {column})")


if 0 not in found_deposits.values():
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
