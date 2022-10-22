lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broken = 0
total_sword_broken = 0
total_shield_broken = 0
total_armor_broken = 0
total_expenses = 0
for current_lost_fight in range (lost_fights_count):
    if current_lost_fight % 2 == 0:
        total_helmet_broken = int(lost_fights_count / 2)

    if current_lost_fight % 3 == 0:
        total_sword_broken = int(lost_fights_count / 3)

    if current_lost_fight % 6 == 0:
        total_shield_broken = int(lost_fights_count / 6)

    if current_lost_fight % 2 == 0:
        total_armor_broken = int(total_shield_broken / 2)

    total_expenses = (total_helmet_broken * helmet_price) + (total_sword_broken * sword_price) + (total_shield_broken * shield_price) + (total_armor_broken * armor_price)

print(f'Gladiator expenses: {total_expenses:.2f} aureus')

