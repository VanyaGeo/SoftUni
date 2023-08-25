products_dict = {}

command = input()

while command != "buy":
    command_ = command.split()
    name = command_[0]
    price = float(command_[1])
    quantity = int(command_[2])

    if name not in products_dict:
        products_dict[name] = [price, quantity] # price е с индекс 0, quantity е с индекс 1
    else:
        products_dict[name][1] += quantity
        if products_dict[name][0] != price:
            products_dict[name][0] = price

    command = input()

for key, value in products_dict.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")

# Beer 2.40 350
# Water 1.25 200
# IceTea 5.20 100
# Beer 1.20 200
# IceTea 0.50 120
# buy

# II
# price_by_product = {}
# quantity_by_product = {}
#
# while True:
#     line = input()
#     if line == "buy":
#         break
#
#     product = line.split()
#     name = product[0]
#     price = float(product[1])
#     quantity = int(product[2])
#
#     price_by_product[name] = price
#     if name in price_by_product:
#         quantity_by_product[name] += quantity
#     else:
#         quantity_by_product[name] = quantity
#
# for name in price_by_product:
#     price = quantity_by_product[name]
#     quantity = quantity_by_product[name]
#     total_price = price * quantity
#     print(f"{name} -> {total_price:.2f}")
