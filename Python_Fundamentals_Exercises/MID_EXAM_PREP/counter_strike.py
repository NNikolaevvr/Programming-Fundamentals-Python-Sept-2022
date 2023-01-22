initial_energy = int(input())
distance = input()
won_battle_counter = 0
energy_left = True
while distance != 'End of battle':
    distance = int(distance)

    initial_energy -= distance
    if initial_energy < 0:
        print(f'Not enough energy! Game ends with {won_battle_counter} won battles and {initial_energy + distance} energy')
        break
    won_battle_counter += 1
    if won_battle_counter % 3 == 0:
        initial_energy += won_battle_counter

    distance = input()

else:

    print(f'Won battles: {won_battle_counter}. Energy left: {initial_energy}')
