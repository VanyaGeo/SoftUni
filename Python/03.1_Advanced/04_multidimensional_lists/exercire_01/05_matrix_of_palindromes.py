rows, columns = [int(x) for x in input().split()]

start_letter = ord("a")

for row in range(start_letter, start_letter + rows):
    for column in range(start_letter, start_letter + columns):
        print(f"{chr(row)}{chr(row + column - start_letter)}{chr(row)}", end=' ')
    print()