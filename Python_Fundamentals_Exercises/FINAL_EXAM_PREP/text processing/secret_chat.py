message = input()
command = input()
while command != 'Reveal':
    command = command.split(":|:")
    if command[0] == 'InsertSpace':
        index = int(command[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif command[0] == 'Reverse':
        if command[1] in message:
            message = message.replace(command[1], "", 1)
            message = message + command[1][::-1]
            print(message)
        else:
            print('error')

    elif command[0] == 'ChangeAll':
        substring, replacement = command[1], command[2]
        message = message.replace(substring, replacement)
        print(message)

    command = input()

if message:
    print(f'You have a new text message: {message}')
