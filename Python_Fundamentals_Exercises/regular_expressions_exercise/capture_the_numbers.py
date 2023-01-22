import re

final_result = []
text = input()
search_pattern = r'\d+'

while text:

    final_result += re.findall(search_pattern, text)

    text = input()

print(' '.join(final_result))