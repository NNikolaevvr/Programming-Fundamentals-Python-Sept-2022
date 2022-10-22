list_items = input().split(", ")

command = input()
get_index = ""
while command != 'Craft!':
    command = command.split(" - ")

    if command[0] == 'Collect':
        if not command[1] in list_items:
            list_items.append(command[1])

    if command[0] == 'Drop':
        if command[1] in list_items:
            list_items.remove(command[1])

    if command[0] == 'Combine Items':
        split = command[1].split(":")
        if split[0] in list_items:
            old_item = list_items.index(split[0])
            list_items.insert(old_item + 1, split[1])

    if command[0] == 'Renew':
        if command[1] in list_items:
            list_items.remove(command[1])
            list_items.append(command[1])

    command = input()
print(*list_items, sep=", ")
