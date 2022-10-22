number_of_electrons = int(input())
current_shell = 0
final_list = []

while 0 < number_of_electrons:
    current_shell +=1
    max_electrons = 2*current_shell**2
    if number_of_electrons >= max_electrons:
        final_list.append(max_electrons)
        number_of_electrons -= max_electrons
    else:
        final_list.append(number_of_electrons)
        number_of_electrons = 0

print(final_list)



