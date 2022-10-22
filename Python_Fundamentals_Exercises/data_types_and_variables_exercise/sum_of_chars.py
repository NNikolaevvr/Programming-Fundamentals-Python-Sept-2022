
number_of_lines = int(input())
sum_code_number = 0
for current_number in range(1, number_of_lines + 1):
    current_letter = input()
    code_number = ord(current_letter)
    sum_code_number += code_number

print(f'The sum equals: {sum_code_number}')
