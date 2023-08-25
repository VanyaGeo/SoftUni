chicken_menu = int(input())*10.35
fish_menu = int(input())*12.40
veggie_menu = int(input())*8.15
delivery = 2.50

price_for_food = chicken_menu+fish_menu+veggie_menu
dessert = 0.2*price_for_food

total_price_food_delivery = price_for_food+dessert+delivery

print(total_price_food_delivery)


