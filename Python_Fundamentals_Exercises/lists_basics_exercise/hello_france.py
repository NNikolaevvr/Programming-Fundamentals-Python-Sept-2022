collection_of_items = input().split("|")
budget = int(input())
list_of_items = []
profit = 0
items_with_profit = []

for current_item in collection_of_items:
    item = current_item.split('->')
    item_price = float(item[1])
    valid = False

    if item[0] == "Clothes" and item_price <= 50:
        valid = True
    elif item[0] == "Shoes" and item_price <= 35:
        valid = True
    elif item[0] == "Accessories" and item_price <= 20.50:
        valid = True

    if valid:
        if budget - item_price < 0:
            break

        budget -= item_price
        list_of_items.append(item_price)

for current_price in list_of_items:
    profit = current_price * 0.40
    final_price = profit + current_price
    items_with_profit.append(final_price)

for item in items_with_profit:
    print(f"{item:.2f}", end=" ")
print()
print(f'Profit: {abs(sum(items_with_profit) - sum(list_of_items)):.2f}')

if sum(items_with_profit) + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')