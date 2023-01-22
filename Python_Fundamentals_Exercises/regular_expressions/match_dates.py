import re

dates = input()
search_pattern = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'
final_result = re.findall(search_pattern, dates)

for date in final_result:
    print(f'Day: {date[0]}, Month: {date[2]}, Year: {date[3]}')
