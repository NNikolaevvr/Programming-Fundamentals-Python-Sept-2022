number_of_rooms = int(input())
current_chairs = 0
current_visitors = 0
total_free_chairs = 0
total_needed_chairs = 0
for current_room in range(1, number_of_rooms + 1):
    chairs, visitors = input().split(" ")
    current_chairs = len(chairs)
    current_visitors = int(visitors)

    difference = current_chairs - current_visitors
    if difference >= 0:
        total_free_chairs += difference
    else:
        total_needed_chairs += abs(difference)
        print(f"{abs(difference)} more chairs needed in room {current_room}")

if total_free_chairs >= total_needed_chairs:
    print(f'Game On, {total_free_chairs} free chairs left')
