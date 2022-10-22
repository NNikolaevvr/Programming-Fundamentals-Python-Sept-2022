def total_price(beverage, num):
    coffee = 1.50
    water = 1.00
    coke = 1.40
    snacks = 2.00

    if beverage == 'coffee':
        return f'{coffee * num:.2f}'
    elif beverage == 'water':
        return f'{water * num:.2f}'
    elif beverage == 'coke':
        return f'{coke * num:.2f}'
    elif beverage == 'snacks':
        return f'{snacks * num:.2f}'


product = input()
number = float(input())

print(total_price(product, number))
