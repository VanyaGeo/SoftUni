price_excursion = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle_price = 2.6 * puzzle_count
doll_price = 3 * doll_count
bear_price = 4.1 * bear_count
minion_price = 8.2 * minion_count
truck_price = 2 * truck_count

total_price = puzzle_price + doll_price + bear_price + minion_price + truck_price
total_toy_count = puzzle_count + doll_count + bear_count + minion_count + truck_count

if total_toy_count >= 50:
    total_price = total_price - total_price * 0.25

rent = total_price * 0.1
final_price = total_price - rent

if final_price >= price_excursion:
    print(f"Yes! {final_price - price_excursion:.2f} lv left.")
else:
    print(f"Not enough money! {price_excursion - final_price:.2f} lv needed.")
