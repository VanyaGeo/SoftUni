query_number = int(input())

query = []

for qr in range(query_number):
    command = [int(x) for x in input().split()]

    if command[0] == 1:
        query.append(command[1])

    elif command[0] == 2:
        if query:
            query.pop()

    elif command[0] == 3:
        if query:
            max_num = max(query)
            print(max_num)

    elif command[0] == 4:
        if query:
            min_num = min(query)
            print(min_num)

query.reverse()

print(*query, sep=", ")
