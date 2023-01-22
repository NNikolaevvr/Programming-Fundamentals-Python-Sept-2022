import re
destinations = []
points = 0
text = input()
pattern = r'(=|/)([A-Z][A-Za-z]{2,})\1'

final_result = re.findall(pattern, text)


for i in final_result:

    destinations.append(i[1])
    points += len(i[1])

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {points}')


