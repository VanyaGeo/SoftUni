open_tabs = int(input())
salary = int(input())

fee = 0
final_salary = 0

for tab in range(1, open_tabs + 1):
    tab_name = input()

    if tab_name == "Facebook":
        fee = fee + 150
    elif tab_name == "Instagram":
        fee = fee + 100
    elif tab_name == "Reddit":
        fee = fee + 50

    final_salary = salary - fee

    if final_salary <= 0:
        print(f"You have lost your salary.")
        break
if final_salary > 0:
    print(final_salary)
