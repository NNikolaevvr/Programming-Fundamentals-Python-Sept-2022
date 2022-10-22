divisor = int(input())
boundary = int(input())
current_number = 0
for current_number in range(boundary, divisor, -1):
    if current_number % divisor == 0:
        break
print(current_number)