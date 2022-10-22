budget = float(input())
price_for_1_kg_flour = float(input())
breads_counter = 0
colored_eggs = 0
pack_of_eggs = price_for_1_kg_flour * 0.75
price_of_milk = price_for_1_kg_flour * 0.25
price_of_milk1 = (price_for_1_kg_flour + price_of_milk) / 4
one_bread_price = price_for_1_kg_flour + pack_of_eggs + price_of_milk1

while budget >= one_bread_price:
    budget -= one_bread_price
    breads_counter += 1
    colored_eggs += 3

    if breads_counter % 3 == 0:
        colored_eggs -= breads_counter - 2

print(f'You made {breads_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')



