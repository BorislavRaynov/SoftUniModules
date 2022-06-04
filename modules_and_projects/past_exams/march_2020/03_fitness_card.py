init_money = float(input())
gender = input()
age = int(input())
type_sport = input()

current_money = 0
if gender == "m":
    if type_sport == "Gym":
        current_money = 42
    elif type_sport == "Boxing":
        current_money = 41
    elif type_sport == "Yoga":
        current_money = 45
    elif type_sport == "Zumba":
        current_money = 34
    elif type_sport == "Dances":
        current_money = 51
    elif type_sport == "Pilates":
        current_money = 39
    if age <= 19:
        current_money = current_money * 0.80
elif gender == "f":
    if type_sport == "Gym":
        current_money = 35
    elif type_sport == "Boxing":
        current_money = 37
    elif type_sport == "Yoga":
        current_money = 42
    elif type_sport == "Zumba":
        current_money = 31
    elif type_sport == "Dances":
        current_money = 53
    elif type_sport == "Pilates":
        current_money = 37
    if age <= 19:
        current_money = current_money * 0.80
if current_money < init_money:
    print(f"You purchased a 1 month pass for {type_sport}.")
else:
    diff = abs(current_money - init_money)
    print(f"You don't have enough money! You need ${diff:.2f} more.")