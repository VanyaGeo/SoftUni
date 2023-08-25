flower = input()
amount_flower = int(input())
budget = int(input())
price = 0

if flower == "Roses":
    price = amount_flower * 5
    if amount_flower > 80:
        price -= price * 0.1
elif flower == "Dahlias":
    price = amount_flower * 3.80
    if amount_flower > 90:
        price -= price * 0.15
elif flower == "Tulips":
    price = amount_flower * 2.80
    if amount_flower > 80:
        price -= price * 0.15
elif flower == "Narcissus":
    price = amount_flower * 3
    if amount_flower < 120:
        price += price * 0.15
elif flower == "Gladiolus":
    price = amount_flower * 2.50
    if amount_flower < 80:
        price += price * 0.2

if budget >= price:
    print(f"Hey, you have a great garden with {amount_flower} {flower} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")