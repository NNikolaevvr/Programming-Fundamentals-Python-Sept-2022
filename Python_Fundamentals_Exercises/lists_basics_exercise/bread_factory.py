working_day_events = input().split("|")
coins = 100
energy = 100
gain_energy = 0
zero_energy = 0
earned_energy = 0
earned_coins = 0
all_orders = True
for current_event in working_day_events:
    event = current_event.split("-")
    if event[0] == 'rest':
        current_energy = int(event[1])

        if energy + current_energy > 100:
            gain_energy = 100 - energy

        else:
            gain_energy = current_energy

        energy += gain_energy
        print(f'You gained {gain_energy} energy.')
        print(f'Current energy: {energy}.')

    elif event[0] == 'order':
        if energy >= 30:
            energy -= 30
            coins += int(event[1])
            print(f'You earned {int(event[1])} coins.')

        else:
            energy += 50
            print(f'You had to rest!')

    else:
        if coins >= int(event[1]):
            coins -= int(event[1])
            print(f'You bought {event[0]}.')

        else:
            print(f'Closed! Cannot afford {event[0]}.')
            all_orders = False

            break

if all_orders:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
