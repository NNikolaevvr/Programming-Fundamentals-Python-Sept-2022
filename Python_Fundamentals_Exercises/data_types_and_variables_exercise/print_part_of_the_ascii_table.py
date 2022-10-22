first_index = int(input())
last_index = int(input())
ord_to_chr = ""

for current_index in range(first_index, last_index +1):
    ord_to_chr = chr(current_index)

    print(ord_to_chr, end= " ")