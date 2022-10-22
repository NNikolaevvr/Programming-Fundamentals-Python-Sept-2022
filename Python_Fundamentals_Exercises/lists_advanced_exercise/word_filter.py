list_of_words = input().split()

new_list = [x for x in list_of_words if len(x) % 2 == 0]

print(*new_list, sep="\n")