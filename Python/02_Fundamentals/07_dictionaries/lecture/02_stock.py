elements = input().split()
products = {}

for element in range(0, len(elements), 2):
    product = elements[element]
    quantity = int(elements[element + 1])
    products[product] = quantity

searched_products = input().split()

for searched_prod in searched_products:
    if searched_prod in products.keys():
        print(f"We have {products[searched_prod]} of {searched_prod} left")
    else:
        print(f"Sorry, we don't have {searched_prod}")

# cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes