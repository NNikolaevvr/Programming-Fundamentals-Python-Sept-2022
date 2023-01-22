number_of_heroes = int(input())
heroes_dict = {}

for i in range(number_of_heroes):
    heroes = input().split(" ")
    hero, hp, mana = heroes[0], int(heroes[1]), int(heroes[2])

    heroes_dict[hero] = [hp, mana]

command = input()

while command != 'End':

    command = command.split(" - ")

    action, hero_name, amount = command[0], command[1], int(command[2])

    if action == 'CastSpell':
        mp_needed = int(command[2])
        spell_name = command[3]

        if hero_name in heroes_dict.keys():
            if heroes_dict[hero_name][1] >= mp_needed:
                heroes_dict[hero_name][1] = heroes_dict[hero_name][1] - mp_needed

                print(f'{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!')
            else:
                print(f'{hero_name} does not have enough MP to cast {spell_name}!')


    elif action == 'TakeDamage':
        damage = int(command[2])
        attacker = command[3]

        if hero_name in heroes_dict.keys():
            heroes_dict[hero_name][0] = heroes_dict[hero_name][0] - damage

            if heroes_dict[hero_name][0] > 0:
                print(
                    f'{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name][0]} HP left!')

            else:

                print(f'{hero_name} has been killed by {attacker}!')
                del heroes_dict[hero_name]

    elif action == 'Recharge':
        initial_mana = heroes_dict[hero_name][1]
        if hero_name in heroes_dict.keys():
            heroes_dict[hero_name][1] = amount + heroes_dict[hero_name][1]
            if heroes_dict[hero_name][1] > 200:
                amount = abs(200 - initial_mana)
                heroes_dict[hero_name][1] = 200

            print(f'{hero_name} recharged for {amount} MP!')

    elif action == 'Heal':
        if hero_name in heroes_dict.keys():
            initial_hp = heroes_dict[hero_name][0]
            heroes_dict[hero_name][0] = amount + heroes_dict[hero_name][0]
            if heroes_dict[hero_name][0] > 100:
                amount = abs(100 - initial_hp)
                heroes_dict[hero_name][0] = 100

            print(f'{hero_name} healed for {amount} HP!')

    command = input()

for key, value in heroes_dict.items():
    print(key)
    print(f'  HP: {value[0]}')
    print(f'  MP: {value[1]}')
