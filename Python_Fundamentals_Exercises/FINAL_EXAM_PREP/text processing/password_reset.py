text = input()

command = input()
password = ''
while command != 'Done':
    command = command.split(" ")

    if command[0] == 'TakeOdd':

        for i in range(1, len(text), 2):
            password += text[i]
        text = password

        print(text)

    elif command[0] == 'Cut':
        index, length = int(command[1]), int(command[2])

        left = text[:index]
        right = text[index + length:]
        text = left + right
        print(text)

    elif command[0] == 'Substitute':
        substring, substitute = command[1], command[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)

        else:
            print(f'Nothing to replace!')

    command = input()

print(f'Your password is: {text}')