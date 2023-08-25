command = input()

company_users_dict = {}

while command != "End":
    command_ = command.split(" -> ")
    company_name = command_[0]
    employee_id = command_[1]

    if company_name not in company_users_dict:
        company_users_dict[company_name] = []

    if employee_id not in company_users_dict[company_name]:
        company_users_dict[company_name].append(employee_id)

    command = input()

for company, employees in company_users_dict.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")

# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End