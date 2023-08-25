resource = input()

resource_dict = {}

while resource != "stop":
    quantity = int(input())
    if resource not in resource_dict.keys():
        resource_dict[resource] = quantity
    else:
        resource_dict[resource] += quantity

    resource = input()

for res in resource_dict.keys():
    print(f"{res} -> {resource_dict[res]}")

# Gold
# 155
# Silver
# 10
# Copper
# 17
# stop