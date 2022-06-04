count_days = int(input())
total_food = float(input())

food_eaten_dog = 0
food_eaten_cat = 0
biscuits_gr = 0
food_for_day = 0

for day in range(1, count_days + 1):
    dog_food = int(input())
    cat_food = int(input())

    food_eaten_dog += dog_food
    food_eaten_cat += cat_food
    food_for_day = dog_food + cat_food
    if day % 3 == 0:
        biscuits_gr += food_for_day * 0.10

eaten_food = food_eaten_cat + food_eaten_dog
percent_eaten_food = (eaten_food / total_food) * 100
percent_dog_food = (food_eaten_dog / eaten_food) * 100
percent_cat_food = (food_eaten_cat / eaten_food) * 100

print(f"Total eaten biscuits: {round(biscuits_gr)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")
