size = int(input())

matrix = []
alice_pos = []

tea_bags = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[row][alice_pos[1]] = '*'

while tea_bags < 10:
    direction = input()

    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row, col]
    position = matrix[row][col]
    matrix[row][col] = '*'

    if position == 'R':
        break

    if position.isdigit():
        tea_bags += int(position)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[' '.join(row) for row in matrix], sep='\n')


# с обяснения:

# size = int(input())  # прочитаме размера на матрицата
#
# matrix = []  # създаваме променлива, в която да пазим матрицата
# alice_pos = []  # създаваме променлива, в която да пазим позицията на Алиса
#
# tea_bags = 0  # създаваме променлива, в която да пазим броя на пакетчетата с чай
#
# directions = {  # създаваме променлива, в която да пазим посоките
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1),
# }
#
# for row in range(size):  # развъртаме цикъл за всеки ред, за да прочетем матрицата
#     matrix.append(input().split())  # прочитаме ред от конзолата, разделяме го по спейс и го добавяме към матрицата
#
#     if 'A' in matrix[row]:  # проверяваме дали Алиса е на този ред
#         alice_pos = [row, matrix[row].index('A')]  # ако да, запазваме реда и колоната на които е Алиса
#         matrix[row][alice_pos[1]] = '*'  # слагаме звезда на позицията на Алиса
#
# while tea_bags < 10:  # развъртаме цикъл, докато Алиса не събере 10 пакетчета с чай
#     direction = input()  # прочитаме посоката на движение
#
#     row = alice_pos[0] + directions[direction][0]  # събираме реда на Алиса с този от посоката
#     col = alice_pos[1] + directions[direction][1]  # събираме колоната на Алиса с тази от посоката
#
#     if not (0 <= row < size and 0 <= col < size):  # проверяваме дали координатите на Алиса са валидни
#         break  # прекратяваме цикъла
#
#     alice_pos = [row, col]  # обновяваме позицията на Алиса
#     position = matrix[row][col]  # запазваме стойността на позицията на Алиса
#     matrix[row][col] = '*'  # променяме стойността на позицията й на звезда
#
#     if position == 'R':  # проверяваме дали Алиса не е попаднала в заешката дупка
#         break  # прекратяваме цикъла
#
#     if position.isdigit():  # проверяваме дали Алиса е стъпила на пакетче с чай
#         tea_bags += int(position)  # увеличаваме броя на пакетчетата, които Алиса е събрала
#
# if tea_bags < 10:  # проверяваме дали Алиса е събрала нужния брой пакетчета, в случая 10
#     print("Alice didn't make it to the tea party.")  # принтираме, че Алиса не е успяла да отиде на партито
# else:
#     print("She did it! She went to the party.")  # принтираме, че Алиса е успяла да отиде на партито
#
# print(*[' '.join(row) for row in matrix], sep='\n')  # принтираме матрицата
