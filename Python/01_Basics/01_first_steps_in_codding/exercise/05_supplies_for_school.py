pen_packages = int(input())*5.80
highlighter_packages = int(input())*7.20
cleansing_agent_letres = int(input())*1.20
discount_percentage = int(input())/100

amount_without_discount = pen_packages+highlighter_packages+cleansing_agent_letres
amount_with_discount = amount_without_discount-(amount_without_discount*discount_percentage)
print(amount_with_discount)
