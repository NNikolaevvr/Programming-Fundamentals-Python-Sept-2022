number = int(input())
word = input()

unfiltered_list = []
filtered_list = []

for current_unfiltered_filter in range(number):
    current_word = input()

    unfiltered_list.append(current_word)

    if word in current_word:
        filtered_list.append(current_word)

print(unfiltered_list)
print(filtered_list)
