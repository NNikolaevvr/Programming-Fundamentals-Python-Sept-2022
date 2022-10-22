quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
budget = 0
christmas_spirit = 0

for current_day in range(1, days_left_until_christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        budget += quantity_of_decorations * ornament_set
        christmas_spirit += 5
    if current_day % 3 == 0:
        budget += (quantity_of_decorations * tree_skirt) + quantity_of_decorations * tree_garland
        christmas_spirit += 13
    if current_day % 5 == 0:
        budget += quantity_of_decorations * tree_lights
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30

    if current_day % 10 == 0:
        christmas_spirit -= 20
        budget += tree_skirt + tree_garland + tree_lights

if days_left_until_christmas % 10 == 0:
    christmas_spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {christmas_spirit}')
