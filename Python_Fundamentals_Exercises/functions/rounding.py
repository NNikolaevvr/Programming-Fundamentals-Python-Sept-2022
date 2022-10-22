def rounding(num):
    numbers_list = []
    for current_num in num:
        numbers_list.append(round(float(current_num)))
    return numbers_list


numbers = input().split(" ")
print(rounding(numbers))
