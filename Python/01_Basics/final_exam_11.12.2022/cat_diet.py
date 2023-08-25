percent_fat = int(input())
percent_protein = int(input())
percent_carbs = int(input())
total_calories = int(input())
percent_water = int(input())

gram_fat = (total_calories * (percent_fat / 100)) / 9
gram_protein = (total_calories * (percent_protein / 100)) / 4
gram_carb = (total_calories * (percent_carbs / 100)) / 4

total_food_gram = gram_fat + gram_protein + gram_carb
calories_per_food = total_calories / total_food_gram
water = (percent_water / 100) * calories_per_food
water_left = 100 - percent_water
calories = (water_left / 100) * calories_per_food

print(f"{calories:.4f}")
