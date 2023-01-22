text = input()
encrypted_message = ""

for i in text:
    ascii_text = ord(i) + 3
    converted = chr(ascii_text)
    encrypted_message += converted

print(encrypted_message)