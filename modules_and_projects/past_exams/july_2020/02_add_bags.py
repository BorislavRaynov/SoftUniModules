price_up_to_20 = float(input())
laguage_kg = float(input())
days_to_traveling = int(input())
count_laguages = int(input())

if laguage_kg < 10:
    price_laguage =  price_up_to_20 * 0.20
elif laguage_kg <= 20:
    price_laguage = price_up_to_20 * 0.50
else:
    price_laguage = price_up_to_20

if days_to_traveling > 30:
    final_price = price_laguage * count_laguages * 1.1
elif 7 <= days_to_traveling <= 30:
    final_price = price_laguage * count_laguages * 1.15
else:
    final_price = price_laguage * count_laguages * 1.4

print(f"The total price of bags is: {final_price:.2f} lv. ")
