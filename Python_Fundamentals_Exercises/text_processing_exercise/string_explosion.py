string = input()
strength = 0
new_text = ''
for i in range(len(string)):
    if strength > 0 and string[i] != ">":
        strength -= 1

    elif string[i] == '>':
        new_text += string[i]
        strength += int(string[i + 1 ])
    else:
        new_text += string[i]

print(new_text)