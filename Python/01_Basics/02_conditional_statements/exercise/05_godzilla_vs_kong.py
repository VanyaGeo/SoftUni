movie_budget = float(input())
actors = int(input())
clothing_price = float(input())

total_clothes_price = clothing_price * actors
decor = movie_budget * 0.1

if actors > 150:
    total_clothes_price -= total_clothes_price * 0.1

final_price = total_clothes_price + decor

if  final_price > movie_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {final_price - movie_budget:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {movie_budget - final_price:.2f} leva left.")

