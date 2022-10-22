def characters_in_between(chr1, chr2):
    characters = []
    for current_character in range(ord(chr1) + 1, ord(chr2)):
        characters.append(chr(current_character))

    return characters


character1 = input()
character2 = input()
result = characters_in_between(character1,character2)

print(*result, sep = " ")
