import re

text = input()
word = input()

search_pattern = fr'\b{word}\b'

final_result = re.findall(search_pattern, text, flags=re.IGNORECASE)

print(len(final_result))
