def price_products(prod, amount):
    final_price = 0
    if prod == "water":
        final_price = amount * 1.00
    elif prod == "coffee":
        final_price = amount * 1.50
    elif prod == "coke":
        final_price = amount * 1.40
    elif prod == "snacks":
        final_price = amount * 2.00
    return final_price


product = input()
amount_of_product = int(input())

print(f"{price_products(product, amount_of_product):.2f}")

