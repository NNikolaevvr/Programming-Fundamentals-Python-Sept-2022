entry = input()
phonebook = {}

while "-" in entry:
    entry = entry.split("-")

    name = entry[0]
    number = entry[1]

    phonebook[name] = number

    entry = input()

for check in range(int(entry)):
    searched_name = input()

    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")