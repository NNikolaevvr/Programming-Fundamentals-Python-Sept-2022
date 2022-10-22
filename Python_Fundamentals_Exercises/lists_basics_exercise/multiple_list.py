factor = int(input())
count = int(input())

multiply = []

for current_number in range(1, count + 1):
    multiplier = factor * current_number
    multiply.append(multiplier)

print(multiply)
