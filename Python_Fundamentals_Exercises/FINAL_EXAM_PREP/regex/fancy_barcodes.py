import re

pattern = r'@(#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z]@#+)'

concat = ''
number_of_barcodes = int(input())

for i in range(number_of_barcodes):

    barcode = input()

    search_pattern = re.findall(pattern, barcode)
    for i in search_pattern:
        barcode = i[1]

    if search_pattern:
        for k in barcode:
            if k.isdigit():
                concat += k
        if concat:
            print(f'Product group: {concat}')
            concat = ''

        else:
            print(f'Product group: 00')


    else:

        print('Invalid barcode')
