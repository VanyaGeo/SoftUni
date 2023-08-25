yard_square_metres=float(input())
price_per_square_metre=7.61
price_landscaping_the_whole_yard=yard_square_metres*7.61
discout=price_landscaping_the_whole_yard*0.18
the_final_price=price_landscaping_the_whole_yard-discout

print(f"The final price is: {the_final_price} lv.")
print(f"The discount is: {discout} lv.")
