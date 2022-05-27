import math

area_sq_m = int(input())
grape_kg_per_m2 = float(input())
ltrs_wine_needed = int(input())
count_workers = int(input())

grape_for_wine = area_sq_m * grape_kg_per_m2 * 0.4
grape_per_one_ltr_wine = 2.5
wine_ltrs = grape_for_wine / grape_per_one_ltr_wine

diff = abs(ltrs_wine_needed - wine_ltrs)

if wine_ltrs < ltrs_wine_needed:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
else:
    wine_per_worker = diff / count_workers
    print(f"Good harvest this year! Total wine: {math.floor(wine_ltrs)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
