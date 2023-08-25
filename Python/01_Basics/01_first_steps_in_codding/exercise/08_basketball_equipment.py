annual_tax_for_training = int(input())
basketball_shoes = annual_tax_for_training-(annual_tax_for_training*0.40)
basketball_equipment = basketball_shoes-(basketball_shoes*0.20)
basketball_ball = basketball_equipment*1/4
basketball_accessories = basketball_ball*1/5

total_price = annual_tax_for_training+basketball_shoes+basketball_equipment+basketball_ball+basketball_accessories

print(total_price)