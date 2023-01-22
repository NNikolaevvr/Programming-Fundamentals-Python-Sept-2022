import re

text = input()
search_pattern = r'\b\_([A-Za-z0-9]+)\b'

final_result = re.findall(search_pattern, text)

print(','.join(final_result))

