current_input = input().split()
words = ''.join(current_input)
chars = {}

for char in words:
    if char not in chars.keys():
        chars[char] = 0
    chars[char] += 1

for characters, occurences in chars.items():
    print(f"{characters} -> {int(occurences)}")