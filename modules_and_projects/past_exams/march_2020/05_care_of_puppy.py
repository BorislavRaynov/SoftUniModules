food_kg = int(input())
food_per_day = input()

food_gr = food_kg * 1000
total_food = 0

while food_per_day != "Adopted":
    food_per_day = int(food_per_day)
    total_food += food_per_day
    food_per_day = input()

diff = abs(food_gr - total_food)
if total_food <= food_gr:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
