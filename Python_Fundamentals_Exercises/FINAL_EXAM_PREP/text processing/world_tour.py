text= input()
command = input()
while command != 'Travel':
    operation = command.split(":")

    if operation[0] == 'Add Stop':
        if 0 <= int(operation[1]) <= len(text):
            text = text[:int(operation[1])] + operation[2] + text[int(operation[1]) :]

    elif operation[0] == "Remove Stop":
        start_index = int(operation[1])
        end_index = int(operation[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            for remove in range(start_index, end_index + 1):
                text = text[:start_index] + text[start_index + 1:]

    if operation[0] == "Switch":
        old_string = operation[1]
        new_string = operation[2]
        if old_string in text:
            text = text.replace(old_string, new_string)


    print(text)
    command = input()
print(f"Ready for world tour! Planned stops: {text}")
