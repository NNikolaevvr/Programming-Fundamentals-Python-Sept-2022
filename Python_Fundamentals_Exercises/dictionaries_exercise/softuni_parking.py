number_of_commands = int(input())
registered_people = {}
for commands in range(number_of_commands):

    people = input().split()
    if people[0] == 'register':
        operation = people[0]
        name = people[1]
        plate = people[2]
        if name not in registered_people:
            registered_people[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f'ERROR: already registered with plate number {plate}')
    elif people[0] == 'unregister':
        operation = people[0]
        name = people[1]
        if name in registered_people:
            registered_people.pop(name)

            print(f'{name} unregistered successfully')
        else:
            print(f'ERROR: user {name} not found')

for name, plate in registered_people.items():
    print(f'{name} => {plate}')
