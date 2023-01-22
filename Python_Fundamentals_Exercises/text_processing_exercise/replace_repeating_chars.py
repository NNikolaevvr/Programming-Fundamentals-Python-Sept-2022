repeating_chars = input()
current_letter = ""
last_letter = ""
final_text = ''
for current_letter in repeating_chars:
    if current_letter != last_letter:
        final_text +=current_letter
        last_letter = current_letter

print(final_text)
