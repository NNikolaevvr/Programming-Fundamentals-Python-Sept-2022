def top_5_numbers(num):
    new_list = []
    for current_num in range(len(num)):
        num[current_num] = int(num[current_num])
    average_num = sum(num) / len(num)
    for i in num:
        if i > average_num:
            new_list.append(i)

    if (len(new_list)) != 0:
        new_list = sorted(new_list, reverse=True)
        return print(*new_list[:5])
    else:
        return print('No')


numbers = input().split(" ")
top_5_numbers(numbers)
