command = input()
employees = {}

while command !='End':
    company_name, employee_id = command.split(" -> ")
    if company_name not in employees:
        employees[company_name] = []
    if employee_id not in employees[company_name]:
        employees[company_name].append(employee_id)


    command = input()

for current_company, employee_ids in employees.items():
    all_employees = '\n-- '.join(employee_ids)
    print(f"{current_company}\n-- {all_employees}")