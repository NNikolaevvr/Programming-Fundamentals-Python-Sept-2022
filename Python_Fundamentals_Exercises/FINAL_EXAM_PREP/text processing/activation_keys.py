text = input()

command = input()

while command != 'Generate':
    command = command.split(">>>")
    if command[0] == 'Contains':
        if command[1] in text:
            print(f'{text} contains {command[1]}')

        else:
            print(f'Substring not found!')

    elif command[0] == 'Flip':
        upper = command[1]
        lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])

        if command[1] == 'Upper':

            text = text[:start_index] + text[start_index:end_index].upper() + text[end_index:]
            print(text)
        elif command[1] == 'Lower':
            text = text[:start_index] + text[start_index:end_index].lower() + text[end_index:]
            print(text)

    elif command[0] == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        left = text[:start_index]
        right = text[end_index:]
        text = left + right
        print(text)

    command = input()

print(f'Your activation key is: {text}')
