command = input()
food_stock = {}

while command != "statistics":
    info_product = command.split(": ")
    key = info_product[0]
    value = int(info_product[1])
    if key in food_stock:
        food_stock[key] += value
    else:
        food_stock[key] = int(value)

    command = input()

print("Products in stock:")
for product, quantity in food_stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(food_stock)}")
print(f"Total Quantity: {sum(food_stock.values())}")
