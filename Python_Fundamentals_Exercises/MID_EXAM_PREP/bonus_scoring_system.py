import math
number_of_students = int(input())
total_number_of_lectures = int(input())
bonus = int(input())
max_bonus = []
total_bonus = 0
student_attendance = 0
if total_number_of_lectures == 0:

    print(f'Max Bonus: 0.')

    print(f'The student has attended 0 lectures.')

else:

    for current_student in range(number_of_students ):
        student_attendance = int(input())
        max_bonus.append(student_attendance)
    total_bonus = math.ceil((max(max_bonus) / total_number_of_lectures) * (5 + bonus))

    print(f'Max Bonus: {total_bonus}.')

    print(f'The student has attended {max(max_bonus)} lectures.')





