employees_happiness = list(map(int, input().split(" ")))
happiness_factor = int(input())
filtered_list = []

employees_happiness = [x * happiness_factor for x in employees_happiness]

average_happiness = sum(employees_happiness) / len(employees_happiness)

for current_employee in employees_happiness:
    if current_employee >= average_happiness:
        filtered_list.append(current_employee)


len_filtered_list = len(filtered_list)

if len_filtered_list >= len(employees_happiness) / 2:
    print(f'Score: {len_filtered_list}/{len(employees_happiness)}. Employees are happy!')

else:
    print(f'Score: {len_filtered_list}/{len(employees_happiness)}. Employees are not happy!')