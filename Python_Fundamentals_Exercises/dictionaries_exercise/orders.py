products = {}
item = input()
quantity = 0
total_price = 0
total_quantity = 0
price = 0
repeated = False
while item != "buy":
    repeated = False
    item = item.split()
    name = item[0]
    price = float(item[1])
    quantity = int(item[2])

    if name in products.keys():
        products[name][0] += quantity
        products[name][1] = price

        repeated = True

    if name not in products.keys():
        products[name] = []
        products[name].append(quantity)
        products[name].append(price)

    item = input()

for product, quantity in products.items():
    total_price = quantity[0] * quantity[1]

    print(f'{product} -> {total_price:.2f}')
