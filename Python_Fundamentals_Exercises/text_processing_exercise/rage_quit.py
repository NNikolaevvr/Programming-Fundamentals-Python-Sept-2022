string = input().upper()
unique_symbols = ""
number = ""
sum_chars = ""
for idx in range(len(string)):
    i = string[idx]
    if not i.isdigit():
        unique_symbols += i

    elif i.isdigit():
        number += i

        if idx + 1 < len(string):
            if string[idx + 1].isdigit():

                continue

        sum_chars += unique_symbols * int(number)

        number = ''
        unique_symbols = ""

print(f'Unique symbols used: {len(set(sum_chars))}')
print(sum_chars)


