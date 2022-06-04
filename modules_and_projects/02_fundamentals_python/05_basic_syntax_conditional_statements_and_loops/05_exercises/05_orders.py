orders = int(input())
total_order = 0

for order in range(1, orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    else:
        price_order = price_per_capsule * days * capsules_per_day
        total_order += price_order
    print(f"The price for the coffee is: ${price_order:.2f}")
print(f"Total: ${total_order:.2f}")
