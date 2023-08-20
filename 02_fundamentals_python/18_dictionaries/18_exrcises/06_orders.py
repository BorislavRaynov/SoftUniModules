command = input()
products = {}

while command != "buy":
    info = command.split()
    type_of_product = info[0]
    price = float(info[1])
    quantity = int(info[2])
    if type_of_product not in products:
        products[type_of_product] = []
        products[type_of_product].append(0)
        products[type_of_product].append(0)
    products[type_of_product][0] = price
    products[type_of_product][1] += quantity
    command = input()

for product, price in products.items():
    print(f'{product} -> {products[product][0] * products[product][1]:.2f}')
