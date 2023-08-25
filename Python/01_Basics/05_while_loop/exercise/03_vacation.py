vacation_needed_money = float(input())
saved_money = float(input())
days_of_spending_money = 0
total_days = 0

while True:

    if days_of_spending_money >= 5:
        print("You can't save the money.")
        print(f"{total_days}")
        break
    if saved_money >= vacation_needed_money:
        print(f"You saved the money for {total_days} days.")
        break

    action = input()
    amount = float(input())
    total_days = total_days + 1

    if action == "spend":
        saved_money = saved_money - amount
        days_of_spending_money = days_of_spending_money + 1
        if saved_money < 0:
            saved_money = 0
    elif action == "save":
        days_of_spending_money = 0
        saved_money = saved_money + amount

