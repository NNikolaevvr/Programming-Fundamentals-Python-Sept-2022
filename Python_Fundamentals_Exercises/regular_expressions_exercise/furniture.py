import re
command = input()
total_money = 0
bought_furniture = []
search_pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)\!(\d+)'
while command != 'Purchase':

    match = re.search(search_pattern, command)
    if match:
        furniture = match.groups()[0]
        price = match.groups()[1]
        quantity = match.groups()[2]

        bought_furniture.append(furniture)
        total_money += float(price) * int(quantity)

    command = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")
