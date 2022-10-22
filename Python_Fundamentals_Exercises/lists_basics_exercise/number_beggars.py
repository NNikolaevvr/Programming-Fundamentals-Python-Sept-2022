amounts = input().split(", ")
number_of_beggars = int(input())
converted_list = []
sum_of_each_beggar = 0
starting_index = 0
final_list = []
for current_amount in amounts:
    converted = int(current_amount)

    converted_list.append(converted)
while starting_index < number_of_beggars:
    sum_of_each_beggar = 0
    for current_beggar in range(starting_index, len(converted_list), number_of_beggars):

        sum_of_each_beggar += converted_list[current_beggar]
    final_list.append(sum_of_each_beggar)
    starting_index += 1
print(final_list)