import re

text = input()
emojis = []
numbers = []
search_pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
cool_threshold = 1
valid_emojis = re.findall(search_pattern, text)
ascii = []
cool_emojis = []
for i in text:
    if i.isdigit():
        numbers.append(int(i))

for k in numbers:
    cool_threshold = k * cool_threshold

print(f'Cool threshold: {cool_threshold}')

for i in valid_emojis:
    emojis.append(i)

print(f'{len(emojis)} emojis found in the text. The cool ones are:')

for emoji in emojis:

    for current_emoji in emoji[1]:
        ascii.append( int(ord(current_emoji)))

    total_sum = sum(ascii)

    if total_sum > cool_threshold:
        cool_emojis.append(emoji)
    ascii.clear()

for i in cool_emojis:
    print(f'{"".join(i)}')
