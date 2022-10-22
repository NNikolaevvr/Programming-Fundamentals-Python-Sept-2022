quantity_of_food = float(input())
quantity_of_hay = float(input())
quantity_of_cover = float(input())
guineas_pig_weight = float(input())

quantity_of_food *= 1000
quantity_of_hay *= 1000
quantity_of_cover *= 1000
guineas_pig_weight *= 1000
go_to_the_store = False
for current_day in range(1, 30 + 1):
    quantity_of_food -= 300
    if current_day % 2 == 0:
        quantity_of_hay -= quantity_of_food * 0.05

    if current_day % 3 == 0:
        quantity_of_cover -= guineas_pig_weight / 3

    if quantity_of_food <= 0 or quantity_of_cover <= 0 or quantity_of_hay <= 0:
        go_to_the_store = True
        break

if go_to_the_store:
    print("Merry must go to the pet store!")

else:
    quantity_of_food /= 1000
    quantity_of_hay /= 1000
    quantity_of_cover /= 1000
    guineas_pig_weight /= 1000
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food:.2f}, Hay: {quantity_of_hay:.2f}, Cover: {quantity_of_cover:.2f}.")
