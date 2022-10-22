def factorial_division(num1, num2):
    sum_first = 1
    sum_second = 1
    for current_num1 in range(1, num1 + 1):
        sum_first *= current_num1

    for current_num2 in range(1, num2 + 1):
        sum_second *= current_num2

    final_result = sum_first / sum_second
    return f'{final_result:.2f}'


first_number = int(input())
second_number = int(input())

print(factorial_division(first_number, second_number))
