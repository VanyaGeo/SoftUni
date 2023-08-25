list_of_employees_happiness = [int(number) for number in input().split()]
factor = int(input())

average = sum(list_of_employees_happiness) / len(list_of_employees_happiness)
happy_employees = [employee for employee in list_of_employees_happiness if employee >= average]

if len(happy_employees) >= (len(list_of_employees_happiness) / 2):
    print(f"Score: {len(happy_employees)}/{len(list_of_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(list_of_employees_happiness)}. Employees are not happy!")

