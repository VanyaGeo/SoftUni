group_budget = int(input())
season = input()
fisherman = int(input())

boat_price = 0
# discount = 0
final_price = 0

if season == "Spring":
    boat_price = 3000

    if fisherman <= 6:
        discount = boat_price * 0.1
        final_price = boat_price - discount

    elif fisherman <= 11:
        discount = boat_price * 0.15
        final_price = boat_price - discount

    elif fisherman >= 12:
        discount = boat_price * 0.25
        final_price = boat_price - discount

elif season == "Summer" or season == "Autumn":
    boat_price = 4200

    if fisherman <= 6:
        discount = boat_price * 0.1
        final_price = boat_price - discount

    elif fisherman <= 11:
        discount = boat_price * 0.15
        final_price = boat_price - discount

    elif fisherman >= 12:
        discount = boat_price * 0.25
        final_price = boat_price - discount

elif season == "Winter":
    boat_price = 2600

    if fisherman <= 6:
        discount = boat_price * 0.1
        final_price = boat_price - discount

    elif fisherman <= 11:
        discount = boat_price * 0.15
        final_price = boat_price - discount

    elif fisherman >= 12:
        discount = boat_price * 0.25
        final_price = boat_price - discount

if fisherman % 2 == 0 and season != "Autumn":
    final_price = final_price * 0.95

price = abs(group_budget - final_price)

if final_price <= group_budget:
    print(f"Yes! You have {price:.2f} leva left.")

else:
    print(f"Not enough money! You need {price:.2f} leva.")
