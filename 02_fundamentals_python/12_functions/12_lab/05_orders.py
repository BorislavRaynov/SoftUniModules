def total_price(a, b):
    result = None
    if a == "coffee":
        result = b * 1.50
    elif a == "water":
        result = b * 1.00
    elif a == "coke":
        result = b * 1.40
    elif a == "snacks":
        result = b * 2.00

    return result


product = input()
quantity = float(input())
print(f"{total_price(product, quantity):.2f}")
