elements = input().split()
bakery = {}

for element in range(0, len(elements), 2):
    food = elements[element]
    quantity = int(elements[element + 1])
    bakery[food] = quantity

print(bakery)


# bread 10 butter 4 sugar 9 jam 12