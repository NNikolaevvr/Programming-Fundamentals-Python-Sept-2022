number_of_people = int(input())
elevator_of_capacity = int(input())

courses = (number_of_people // elevator_of_capacity)


if number_of_people % elevator_of_capacity != 0:
    courses += 1


print(courses)