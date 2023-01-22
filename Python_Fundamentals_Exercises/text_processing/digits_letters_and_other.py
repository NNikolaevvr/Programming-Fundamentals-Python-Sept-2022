symbols = input()
numbers = []
characters = []
other = []
for character in symbols:
    if character.isdigit():
        numbers.append(character)

    elif character.isalpha():
        characters.append(character)

    else:
        other.append(character)

print(''.join(numbers))
print(''.join(characters))
print(''.join(other))