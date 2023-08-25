budget = float(input())
season = input()

destination = ""
journey_type = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        journey_type = "Camp"
        price = budget * 0.7
    elif season == "winter":
        journey_type = "Hotel"
        price = budget * 0.3

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        journey_type = "Camp"
        price = budget * 0.6
    elif season == "winter":
        journey_type = "Hotel"
        price = budget * 0.2

elif budget > 1000:
    destination = "Europe"
    journey_type = "Hotel"
    price = budget * 0.1

print(f"Somewhere in {destination}")
print(f"{journey_type} - {budget - price:.2f}")
