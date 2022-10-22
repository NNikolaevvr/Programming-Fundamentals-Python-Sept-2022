def even_num(num1):
    filtered_num = []
    for current_num in num1:
        if int(current_num) % 2 == 0:
            filtered_num.append(int(current_num))
    return filtered_num


numbers = input().split(" ")

print(even_num(numbers))
