def functions_nums(first, second, operator):
    if operator == 'multiply':
        return first * second
    elif operator == 'divide':
        return int(first / second)
    elif operator == 'add':
        return first + second
    elif operator == 'subtract':
        return first - second


operation = input()
first_num = int(input())
second_num = int(input())

print(functions_nums(int(first_num), int(second_num), operation))
