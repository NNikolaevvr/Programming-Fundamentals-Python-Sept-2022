def perfect_number(num1):
    sum = 0
    for current_num in range(1, num1):
        if num1 % current_num == 0:
            sum += current_num
    if sum == num1:
        return 'We have a perfect number!'
    return 'It\'s not so perfect.'

number = int(input())

print(perfect_number(number))

