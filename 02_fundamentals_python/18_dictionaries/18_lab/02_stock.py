products = input().split()
searched_products = input().split()
food_products = {}
for product in range(0, len(products), 2):
    key = products[product]
    value = products[product + 1]
    food_products[key] = int(value)
for item in searched_products:
    if item in food_products:
        print(f"We have {food_products.get(item)} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
