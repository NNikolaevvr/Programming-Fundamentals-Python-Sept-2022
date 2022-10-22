def min_max_sum(num1):
    sum_numbers = 0
    for current_number in range(len(num1)):
        num1[current_number] = int(num1[current_number])


    min_num = min(num1)
    max_num = max(num1)
    sum_numbers = sum(num1)

    return min_num, max_num, sum_numbers


numbers = input().split(" ")
min_num, max_num, sum_numbers = min_max_sum(numbers)
print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_numbers}")
