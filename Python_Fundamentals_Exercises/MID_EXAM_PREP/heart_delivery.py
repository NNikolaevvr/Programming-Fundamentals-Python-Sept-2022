neighborhood = [int(x) for x in input().split("@")]
command = input()
house = 0
while command != 'Love!':
    command = command.split(" ")
    index = int(command[1])
    house += index

    if house >= len(neighborhood):
        house = 0

    if neighborhood[house] == 0:
        print(f"Place {house} already had Valentine's day.")
    else:
        neighborhood[house] -= 2
        if neighborhood[house] == 0:
            print(f"Place {house} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {house}.")
count = 0
for house in range(len(neighborhood)):
    if neighborhood[house] > 0:
        count += 1

if count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count} places.")








