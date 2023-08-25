month = input()
nights_amount = int(input())

Apartment = 0
Studio = 0

if month == "May" or month == "October":
    Studio = nights_amount * 50
    Apartment = nights_amount * 65
    if 7 < nights_amount <= 14:
        Studio = Studio - (Studio * 0.05)
    elif nights_amount > 14:
        Studio = Studio - (Studio * 0.3)
        Apartment = Apartment - (Apartment * 0.1)

elif month == "June" or month == "September":
    Studio = nights_amount * 75.20
    Apartment = nights_amount * 68.70
    if nights_amount > 14:
        Studio = Studio - (Studio * 0.2)
        Apartment = Apartment - (Apartment * 0.1)

elif month == "July" or month == "August":
    Studio = nights_amount * 76
    Apartment = nights_amount * 77
    if nights_amount > 14:
        Apartment = Apartment - (Apartment * 0.1)

print(f"Apartment: {Apartment:.2f} lv.")
print(f"Studio: {Studio:.2f} lv.")
