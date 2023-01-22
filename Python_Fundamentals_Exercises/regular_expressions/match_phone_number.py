import re
text = input()
search_pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

final_result = re.findall(search_pattern, text)

print(", ".join(final_result))