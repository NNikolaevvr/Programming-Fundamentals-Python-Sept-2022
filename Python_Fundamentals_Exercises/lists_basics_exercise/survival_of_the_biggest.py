list_of_integer = input().split(" ")
count_of_numbers_to_remove = int(input())
converted_list = []
string_converted = ""

for current_number in list_of_integer:
    converted = int(current_number)

    converted_list.append(converted)

for i in range(count_of_numbers_to_remove):
    small = min(converted_list)
    converted_list.remove(small)

print(*converted_list, sep = ", ")
