days = int(input())
room_type = input()
rate = input()

nights = days - 1

room_for_one_person = nights * 18
apartment = nights * 25
president_apartment = nights * 35
price = 0


if room_type == "room for one person":
    price = room_for_one_person
elif room_type == "apartment":
    if days < 10:
        price = apartment * 0.7
    elif 10 <= days <= 15:
        price = apartment * 0.65
    else:
        price = apartment * 0.5
elif room_type == "president apartment":
    if days < 10:
        price = president_apartment * 0.9
    elif 10 <= days <= 15:
        price = president_apartment * 0.85
    else:
        price = president_apartment * 0.8

if rate == "positive":
    price = price + price * 0.25
else:
    price = price - price * 0.1

print(f"{price:.2f}")

