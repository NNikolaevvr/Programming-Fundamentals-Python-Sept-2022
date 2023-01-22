number_of_pieces = int(input())

pieces_dict = {}
for i in range(number_of_pieces):
    text = input().split('|')
    piece, composer, key = text[0], text[1], text[2]
    pieces_dict[piece] = [composer, key]

command = input()

while command != 'Stop':
    command = command.split("|")
    type_command = command[0]
    p = command[1]
    if type_command == 'Add':
        c = command[2]
        k = command[3]
        if p in pieces_dict:
            print(f"{p} is already in the collection!")
        else:
            pieces_dict[p] = [c, k]
            print(f"{p} by {c} in {k} added to the collection!")

    elif type_command == 'Remove':
        if p in pieces_dict:
            del pieces_dict[p]
            print(f"Successfully removed {p}!")
        else:
            print(f"Invalid operation! {p} does not exist in the collection.")

    elif type_command == 'ChangeKey':
        new_key = command[2]
        if p in pieces_dict:
            pieces_dict[p][1] = new_key
            print(f"Changed the key of {p} to {new_key}!")
        else:
            print(f"Invalid operation! {p} does not exist in the collection.")

    command = input()

for piece in pieces_dict:
    print(f"{piece} -> Composer: {pieces_dict[piece][0]}, Key: {pieces_dict[piece][1]}")