def move(direction, steps):
    row = my_position[0] + (directions[direction][0] * steps)
    column = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= row < size and 0 <= column < size):
        return my_position

    if field[row][column] == "x":
        return my_position

    return [row, column]


def shoot(direction):
    row = my_position[0] + directions[direction][0]
    column = my_position[1] + directions[direction][1]

    while 0 <= row < size and 0 <= column < size:
        if field[row][column] == "x":
            field[row][column] = "."
            return [row, column]

        row += directions[direction][0]
        column += directions[direction][1]


size = 5

field = []
target_amount = 0
hit_targets = 0
hit_targets_positions = []
my_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    field.append(input().split())

    if "A" in field[row]:
        my_position = [row, field[row].index("A")]

    target_amount += field[row].count("x")


for _ in range(int(input())):
    command = input().split()

    if command[0] == "move":
        my_position = move(command[1], int(command[2]))

    elif command[0] == "shoot":
        shoot_targets = shoot(command[1])

        if shoot_targets:
            hit_targets_positions.append(shoot_targets)
            hit_targets += 1

        if hit_targets == target_amount:
            print(f"Training completed! All {target_amount} targets hit.")
            break

else:
    print(f"Training not completed! {target_amount - hit_targets} targets left.")

print(*hit_targets_positions, sep="\n")
