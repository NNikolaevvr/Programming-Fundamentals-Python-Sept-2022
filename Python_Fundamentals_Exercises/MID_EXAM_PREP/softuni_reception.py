employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
student_count = int(input())
hour_needed = 0
left_students = 0

students_per_hour = employee1 + employee2 + employee3

while student_count > 0:
    student_count -= students_per_hour
    hour_needed += 1

    if hour_needed % 4 == 0:
        hour_needed += 1

print(f'Time needed: {hour_needed}h.')
