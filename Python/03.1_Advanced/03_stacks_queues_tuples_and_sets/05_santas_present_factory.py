from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()

    product = material * magic

    if material == 0 and magic == 0:
        continue

    if material == 0:
        magic_levels.appendleft(magic)
        continue
    elif magic == 0:
        materials.append(material)
        continue

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic)
    elif product > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

# [print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
for toy in sorted(crafted):
    print(f"{toy}: {crafted.count(toy)}")

