def sum_even_and_odd_numbers(num1):
    even_num = 0
    odd_num = 0
    for current_number in num1:

        if int(current_number) % 2 == 0:
            even_num += int(current_number)

        else:
            odd_num += int(current_number)

    return f'Odd sum = {odd_num}, Even sum = {even_num}'


number1 = input()

print(sum_even_and_odd_numbers(number1))
