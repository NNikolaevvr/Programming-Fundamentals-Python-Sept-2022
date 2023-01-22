

















text = input()
start_index = 5
end_index = 10

# Remove characters from starting index to ending index

for remove in range(start_index, end_index + 1):
    text = text[:start_index] + text[start_index + 1:]


print(text)


# проверка за валиден индекс:
# if 0 <= index <= len(shelf_of_books)


#Insert an item
#    if operation[0] == 'Add Stop':
#if 0 <= int(operation[1]) <= len(text):
#            text = text[:int(operation[1])] + operation[2] + text[int(operation[1]) :]
#


#if operation[0] == "Switch":
#    old_string = operation[1]
#    new_string = operation[2]
#   if old_string in text:
#       text = text.replace(old_string, new_string)


#if language not in languages.keys():
#    languages[language] = 0
#languages[language] +=


#    if name not in students.keys():
#       students[name] = []
#    students[name].append(grade)