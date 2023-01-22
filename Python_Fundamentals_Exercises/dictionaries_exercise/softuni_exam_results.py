command = input()
dictionary = {}
languages = {}
while command != 'exam finished':
    if 'banned' in command:
        username, ban = command.split("-")
        dictionary.pop(username)
    else:
        username, language, points = command.split("-")
        if username not in dictionary.keys():
            dictionary[username]= []
        dictionary[username].append(int(points))
        if language not in languages.keys():
            languages[language] = 0
        languages[language] +=1

    command = input()

print("Results:")


for student, points in dictionary.items():
    print(f'{student} | {max(points)}')

print("Submissions:")
for language in languages.keys():

    print(f'{language} - {languages[language]}')

