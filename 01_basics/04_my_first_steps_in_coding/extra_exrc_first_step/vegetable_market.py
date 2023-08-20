price_veg_kg = float(input())
price_frts_kg = float(input())
count_veg_kg = int(input())
count_frts_kg = int(input())

incm = price_veg_kg * count_veg_kg + price_frts_kg * count_frts_kg
incm_eur = incm / 1.94
print(f'{incm_eur:.2f}')
