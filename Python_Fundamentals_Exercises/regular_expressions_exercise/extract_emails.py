import re

search_pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b'

text = input()

emails = re.findall(search_pattern, text)
for email in emails:
    print(email[0])