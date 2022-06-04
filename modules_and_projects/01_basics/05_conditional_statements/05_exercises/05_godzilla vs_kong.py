budget = float(input())
statist = int(input())
price_clothes_per_st = float(input())

decor = budget * 0.1
price_st_total = statist * price_clothes_per_st
if statist > 150:
    price_st_total = price_st_total * 0.9

total_price = decor + price_st_total
diff = abs(total_price - budget)

if total_price <= budget:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')