def shopping_list(budget, **kwargs):
    current_amount = int(budget)
    if current_amount < 100:
        return "You do not have enough budget."
    my_basket = {}
    products_info = {}
    count_products = len(products_info)
    result = ''

    for product, info in kwargs.items():
        if product not in products_info:
            products_info[product] = []
        products_info[product].append(float(info[0]))
        products_info[product].append(int(info[1]))

    for key, value in products_info.items():
        amount_needed_to_buy = value[0] * value[1]
        if count_products == len(products_info):
            break
        if amount_needed_to_buy <= current_amount:
            current_amount -= amount_needed_to_buy
            my_basket[key] = amount_needed_to_buy
        count_products += 1
        if len(my_basket) == 5:
            break

    for key, value in my_basket.items():
        result += f"You bought {key} for {value:.2f} leva.\n"

    return result


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


