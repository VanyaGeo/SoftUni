nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours = int(input())

nylon_final = (nylon+2)*1.50
paint_final = (paint+(0.1*paint))*14.50
paint_thinner_final = paint_thinner*5.00
bags = 0.40
price_materials = nylon_final+paint_final+paint_thinner_final+bags
repairmen_price_per_hour = (price_materials*0.3)*hours

price_for_repainting = price_materials+repairmen_price_per_hour

print(price_for_repainting)
