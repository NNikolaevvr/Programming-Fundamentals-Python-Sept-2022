def ascending_order(num1):
    for current_number in range(len(num1)):
        num1[current_number] = int(num1[current_number])
    sort_list = sorted(num1)

    return sort_list


numbers = input().split(" ")

print(ascending_order(numbers))
