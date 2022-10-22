first_string = input().split(", ")
second_string = input().split(", ")
new_list = []

for current_string in first_string:
    for current_string1 in second_string:
        if current_string in current_string1 and current_string not in new_list:
            new_list.append(current_string)

print(new_list)
