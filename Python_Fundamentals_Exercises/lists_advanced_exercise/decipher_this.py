message = input().split(" ")
value = []

new_string = []
num = 0
final_list = []
for current_message in message:
    new_string.clear()
    final_list.clear()
    for i in current_message:
        if i.isdigit():
            new_string.append(i)
    join_numbers = int(''.join(new_string))
    character = chr(join_numbers)
    final_list.append(character)
    for j in current_message:
        if not j.isdigit():
            final_list.append(j)

    final_list[1], final_list[-1] = final_list[-1], final_list[1]
    value.append("".join(final_list))

print(" ".join(value))




