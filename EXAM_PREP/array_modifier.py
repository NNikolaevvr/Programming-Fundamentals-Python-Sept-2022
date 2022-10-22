values = input().split(" ")
command = input().split(" ")
converted_list = []
is_command_decrease = False
decrease_list = []
for current_num in values:
    values = int(current_num)
    converted_list.append(values)

while command[0] != 'end':
    if command[0] == 'swap':
        converted_list[int(command[1])], converted_list[int(command[2])] = converted_list[int(command[2])], \
                                                                           converted_list[int(command[1])]
    elif command[0] == 'multiply':
        converted_list[int(command[1])] *= converted_list[int(command[2])]

    if command[0] == 'decrease':
        for current_index in range(len(converted_list)):
            converted_list[current_index] -= 1


    command = input().split(" ")

print(*converted_list, sep=", ")
