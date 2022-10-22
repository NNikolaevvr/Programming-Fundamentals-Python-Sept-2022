lst = [0]
wagons = int(input())
total_wagons = lst * wagons
command = input()

while command != 'End':
    command = command.split(" ")

    if command[0] == 'add':
        total_wagons[-1] += int(command[1])

    elif command[0] == 'insert':
        total_wagons[int(command[1])] += int(command[2])

    elif command[0] == 'leave':
        total_wagons[int(command[1])] -= int(command[2])

    command = input()

print(total_wagons)


