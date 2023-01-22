import re

text = input()
search_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

final_result = re.findall(search_pattern, text)

print(" ".join(final_result))