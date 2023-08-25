lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toy_amount = 0
present_money_years = 0
present_money_amount = 0
all_present_money = 0
all_toy_price = 0
all_money = 0

for year in range(1, lily_age + 1):
    if year % 2 == 0:
        present_money_years += 1
        present_money_amount = present_money_amount + 10
        all_present_money = all_present_money + present_money_amount

    else:
        toy_amount += 1
        all_toy_price = toy_amount * toy_price

all_money = (all_toy_price + all_present_money) - present_money_years

if all_money >= washing_machine_price:
    print(f"Yes! {all_money - washing_machine_price:.2f}")
else:
    print(f"No! {abs(all_money - washing_machine_price):.2f}")
