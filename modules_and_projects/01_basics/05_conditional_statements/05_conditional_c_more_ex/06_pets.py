import math
count_days = int(input())
total_food_kg = int(input())
dog_per_day_kg = float(input())
cat_per_day_kg = float(input())
turtle_per_day_kg = float(input())

total_dog_food = count_days * dog_per_day_kg
total_cat_food = count_days * cat_per_day_kg
total_turtle_food = count_days * turtle_per_day_kg / 1000

total_food_needed = total_dog_food + total_cat_food + total_turtle_food

diff = abs(total_food_kg - total_food_needed)

if total_food_kg >= total_food_needed:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")