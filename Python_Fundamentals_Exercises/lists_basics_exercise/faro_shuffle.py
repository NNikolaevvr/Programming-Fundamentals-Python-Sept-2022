cards = input().split(" ")
shuffles = int(input())

for current_shuffle in range (shuffles):
    cards_after_shuffle = []

    middle_split = len(cards) // 2

    left_part = cards[:middle_split]
    right_part = cards[middle_split:]

    for current_card in range(len(left_part)):
        cards_after_shuffle.append(left_part[current_card])
        cards_after_shuffle.append(right_part[current_card])
    cards = cards_after_shuffle

print(cards_after_shuffle)