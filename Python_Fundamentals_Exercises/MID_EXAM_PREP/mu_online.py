health = 100
bitcons = 0
total_bitcons = 0
number_of_rooms = input().split("|")

for current_room in number_of_rooms:
    command, number = current_room.split(" ")
    number = int(number)

    if command == 'potion':
        current_health = health
        health += number
        if health > 100:
            health = 100

            print(f'You healed for {100 - current_health} hp.')
            print(f'Current health: {health} hp.')
        else:
            print(f'You healed for {number} hp.')
            print(f'Current health: {health} hp.')

    elif command == 'chest':
        bitcons = number
        total_bitcons += number

        print(f'You found {bitcons} bitcoins.')

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")

        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {number_of_rooms.index(current_room) + 1}')
            break

if health > 0:
    print(f"You've made it!")
    print(f'Bitcoins: {total_bitcons}')
    print(f'Health: {health}')
