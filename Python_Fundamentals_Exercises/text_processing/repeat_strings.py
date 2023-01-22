words = input().split()
final_list = []
for word in words:
    characters = word * len(word)
    final_list.append(characters)
print(''.join(final_list))