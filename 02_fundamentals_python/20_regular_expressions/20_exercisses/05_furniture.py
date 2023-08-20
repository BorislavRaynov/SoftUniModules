import re

info_data = input()
bought_items = []
prices = []
validity = r'>>([a-zA-Z]+)<<([0-9]+[\.0-9]*)!([0-9]+)'

while info_data != "Purchase":
    result = re.findall(validity, info_data)
    for match in result:
        bought_items.append(match[0])
        if "." in match[1]:
            prices.append(float(match[1]) * int(match[2]))
        else:
            prices.append(int(match[1]) * int(match[2]))
    info_data = input()

print("Bought furniture:")
for furniture in bought_items:
    print(furniture)
print(f"Total money spend: {sum(prices):.2f}")
