number_people = int(input())
season = input()
price = 0

if number_people <= 5:
    if season == "spring":
        price = number_people * 50
    elif season == "summer":
        price = number_people * 48.50
        price = price - (price * 0.15)
    elif season == "autumn":
        price = number_people * 60
    elif season == "winter":
        price = number_people * 86
        price = price + (price * 0.08)
elif number_people > 5:
    if season == "spring":
        price = number_people * 48
    elif season == "summer":
        price = number_people * 45
        price = price - (price * 0.15)
    elif season == "autumn":
        price = number_people * 49.50
    elif season == "winter":
        price = number_people * 85
        price = price + (price * 0.08)

print(f"{price:.2f} leva.")

