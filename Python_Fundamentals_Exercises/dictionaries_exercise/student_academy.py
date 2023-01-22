number_of_students = int(input())
students = {}
for current_student in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in students.keys():
        students[name] = []
    students[name].append(grade)

for student, grades in students.items():
    sum_grade = sum(grades)
    average_grade = sum_grade / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")


