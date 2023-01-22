command = input()
students = {}
while command != 'end':
    command = command.split(" : ")
    course = command[0]
    name = command[1]

    if course not in students.keys():
        students[course] = []
    if name not in students[course]:
        students[course].append(name)

    command = input()

for course,student in students.items():
    print(f"{course}: {len(student)}")
    all_students = '\n-- '.join(students[course])
    print(f"-- {all_students}")
