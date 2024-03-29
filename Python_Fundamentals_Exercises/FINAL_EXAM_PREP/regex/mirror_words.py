import re

text = input()
pattern = r'(@|#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1'

result = re.findall(pattern, text)

mirror_words = []
count_of_mirror_words = 0

for pair in result:

    if pair[1] == pair[3][::-1]:
        mirror_words.append(f'{pair[1]} <=> {pair[3]}')
    count_of_mirror_words +=1

if count_of_mirror_words > 0:
    print(f"{count_of_mirror_words} word pairs found!")
    if not mirror_words:
        print(f"No mirror words!")
    else:
        print(f'The mirror words are:')
        print(", ".join(mirror_words))

else:
    print(f'No word pairs found!')
    print(f"No mirror words!")
