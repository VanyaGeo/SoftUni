"""
- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
"""


rows = 8

matrix = []
positions = [[], []] # [[5, 1], [0, 6]]

row_position = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
column_position = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

for row in range(rows):
    matrix.append(input().split())

    if "w" in matrix[row]:
        positions[0].append(row)
        positions[0].append(matrix[row].index("w"))

    if "b" in matrix[row]:
        positions[1].append(row)
        positions[1].append(matrix[row].index("b"))

game_over = False
turn = 0
while True:

    if abs(positions[0][1] - positions[1][1]) == 1 and abs(positions[0][0] - positions[1][0]) == 1:

        if turn % 2 == 0:
            current_position = column_position[positions[1][1]] + row_position[positions[1][0]]
            print(f"Game over! White win, capture on {current_position}.")
            game_over = True
            break

        elif turn % 2 == 1:
            current_position = column_position[positions[0][1]] + row_position[positions[0][0]]
            print(f"Game over! Black win, capture on {current_position}.")
            game_over = True
            break

    if positions[0][0] == 0:
        current_position = column_position[positions[0][1]] + row_position[positions[0][0]]
        print(f"Game over! White pawn is promoted to a queen at {current_position}.")
        break

    elif positions[1][0] == 7:
        current_position = column_position[positions[1][1]] + row_position[positions[1][0]]
        print(f"Game over! Black pawn is promoted to a queen at {current_position}.")
        break

    if turn % 2 == 0:
        positions[0][0] -= 1
    if turn % 2 == 1:
        positions[1][0] += 1

    turn += 1
