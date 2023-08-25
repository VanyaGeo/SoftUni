command = input()

products = {}

while command != "statistics":
    key, value = command.split(": ")
    value = int(value)
    if key in products.keys():
        products[key] += value
    else:
        products[key] = value
    command = input()

print("Products in stock:")

for key, value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products.keys())} \nTotal Quantity: {sum(products.values())}")

# bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics