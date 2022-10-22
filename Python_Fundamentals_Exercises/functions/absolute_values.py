def absolute_values(num):
    list_values = []
    for current_number in num:
        conversion = float(current_number)
        list_values.append(abs(conversion))
    return list_values


numbers = input().split(" ")

print(absolute_values(numbers))
