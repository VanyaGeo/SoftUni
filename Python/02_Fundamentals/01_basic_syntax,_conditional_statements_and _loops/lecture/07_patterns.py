number = int(input())

for rows in range(1, number+1):
    for columns in range(1, rows+1):
        print("*", end="")
    print("")
for rows in range(number, 1, -1):
    for columns in range(rows, 1, -1):
        print("*", end="")
    print("")
