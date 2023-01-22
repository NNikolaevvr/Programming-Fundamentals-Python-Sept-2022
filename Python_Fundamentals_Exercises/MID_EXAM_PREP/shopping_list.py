items = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    if command[0] == 'Urgent':
        if command[1] not in items:
            items.insert(0, command[1])

    elif command[0] == 'Unnecessary':
        if command[1] in items:
            items.remove(command[1])

    if command[0] == 'Correct':
        if command[1] in items:
            item_index = items.index(command[1])
            items.remove(command[1])

            items.insert(item_index, command[2])

    elif command[0] == 'Rearrange':
        if command[1] in items:
            items.remove(command[1])
            items.append(command[1])
    command = input()
print(*items, sep=", ")

