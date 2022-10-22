def sum_numbers(num1, num2):
    sum_nums = num1 + num2
    return sum_nums


def subtract(sum_nums, num3):
    subtract_num = sum_nums - num3
    return subtract_num


def add_and_subtract(num1, num2, num3):
    sum_first_and_second = sum_numbers(num1,num2)
    result = subtract(sum_first_and_second, num3)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num,second_num,third_num))
