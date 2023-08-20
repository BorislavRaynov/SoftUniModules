items_for_sale = input().replace("->", "|").split("|")
budget = float(input())

current_budget = budget
price_for_all_items = 0
train_ticket = 150
current_price_item = 0
new_prices_list = []


for element in range(len(items_for_sale)):
    if items_for_sale[element] == "Shoes":
        current_price_item = float(items_for_sale[element + 1])
        if current_price_item <= 35.00 and current_price_item <= current_budget:
            current_budget -= current_price_item
            price_for_all_items += current_price_item
            new_price = f"{current_price_item * 1.40:.2f}"
            new_prices_list.append(new_price)

    elif items_for_sale[element] == "Clothes":
        current_price_item = float(items_for_sale[element + 1])
        if current_price_item <= 50.00 and current_price_item <= current_budget:
            current_budget -= current_price_item
            price_for_all_items += current_price_item
            new_price = f"{current_price_item * 1.40:.2f}"
            new_prices_list.append(new_price)

    elif items_for_sale[element] == "Accessories":
        current_price_item = float(items_for_sale[element + 1])
        if current_price_item <= 20.50 and current_price_item <= current_budget:
            current_budget -= current_price_item
            price_for_all_items += current_price_item
            new_price = f"{current_price_item * 1.40:.2f}"
            new_prices_list.append(new_price)


new_price_all_items = price_for_all_items * 1.40
profit = new_price_all_items - price_for_all_items

print(*new_prices_list)
print(f"Profit: {profit:.2f}")
if new_price_all_items + current_budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
