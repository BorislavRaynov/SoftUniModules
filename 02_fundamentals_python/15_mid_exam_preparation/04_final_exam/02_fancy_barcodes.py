import re
num = int(input())
pattern = r'@#+[A-Z]([A-Za-z0-9]{4,})[A-Z]@#+'

for data in range(num):
    barcode = input()
    valid_barcode = re.search(pattern, barcode)
    if valid_barcode:
        current_group = re.findall(r'\d', valid_barcode.group(1))
        if current_group:
            print(f"Product group: {''.join(current_group)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
