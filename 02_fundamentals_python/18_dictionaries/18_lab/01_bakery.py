data = input().split()
bakery = {}
for element in range(0, len(data), 2):
    key = data[element]
    value = data[element + 1]
    bakery[key] = int(value)
print(bakery)
