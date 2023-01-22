words = input().split(", ")

valid_word = ''
is_valid = False
length = False
space = False
characters = False
for word in words:


    if 3 <= len(word) <= 16:
        length = True
    else:
        length = False

    if word.isalnum() or '_' in word or  '-' in word:
        characters = True
    else:
        characters = False


    if " " not in word:
        space = True

    else:
        space = False

    if characters == True and space == True and length == True:
        valid_word = word
        print(valid_word)
