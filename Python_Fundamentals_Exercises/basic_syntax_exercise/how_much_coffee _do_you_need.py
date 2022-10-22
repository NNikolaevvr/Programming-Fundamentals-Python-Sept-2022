command = ''
coffee_needed_to_drink = 0

while command != "END":
    command = input()
    if command == "dog" or command == 'cat' or command == 'coding' or command == 'movie':
        coffee_needed_to_drink += 1
    elif command == "DOG" or command == 'CAT' or command == 'CODING' or command == 'MOVIE':
        coffee_needed_to_drink += 2

if coffee_needed_to_drink > 5:
    print('You need extra sleep')
else:
    print(coffee_needed_to_drink)

