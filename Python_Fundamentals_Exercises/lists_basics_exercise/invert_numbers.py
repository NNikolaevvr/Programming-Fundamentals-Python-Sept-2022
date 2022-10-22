number = input().split(" ")
inverted_number = []


for current_number in number:
    opposite = -int(current_number)
    inverted_number.append(opposite)

print(inverted_number)

