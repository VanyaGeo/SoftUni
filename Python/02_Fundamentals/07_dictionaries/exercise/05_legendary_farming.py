legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
is_obtained = False
command = input().split()

while command:
    for index in range(0, len(command), 2):
        key = command[index + 1].lower()
        value = int(command[index])

        if key in legendary_items:
            legendary_items[key] += value
            if legendary_items[key] >= 250:
                if key == "shards":
                    print("Shadowmourne obtained!")
                if key == "fragments":
                    print("Valanyr obtained!")
                if key == "motes":
                    print("Dragonwrath obtained!")

                legendary_items[key] -= 250
                is_obtained = True
                break
        else:
            if key not in junk:
                junk[key] = 0
            junk[key] += value
    if is_obtained:
        break
    command = input().split()

for material, quantity in legendary_items.items():
    print(f"{material}: {quantity}")
for material, quantity in junk.items():
    print(f"{material}: {quantity}")


# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards