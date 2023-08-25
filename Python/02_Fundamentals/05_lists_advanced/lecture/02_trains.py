wagons = int(input())
train = [0] * wagons

command = input()

while command != "End":
    action = command.split()[0]
    if action == "add":
        people = int(command.split()[1])
        train[-1] += people  #  [-1] това е винаги последният индекс от даден лист

    elif action == "insert":
        index = int(command.split()[1])
        people = int(command.split()[2])
        train[index] += people

    elif action == "leave":
        index = int(command.split()[1])
        people = int(command.split()[2])
        train[index] -= people

    command = input()

print(train)

# command.split()[индекс - 1, 2, 3 ..] ==> превръщаме командата в лист и взимаме съответния индекс от листа