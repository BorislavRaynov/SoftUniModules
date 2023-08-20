count_dancers = int(input())
count_points = float(input())
type_season = input()
type_location = input()

total_price = count_dancers * count_points

if type_location == "Bulgaria":
    total_price = total_price
    if type_season == "summer":
        total_price = total_price * 0.95
    elif type_season == "winter":
        total_price = total_price * 0.92
elif type_location == "Abroad":
    total_price = total_price * 1.50
    if type_season == "summer":
        total_price = total_price * 0.90
    elif type_season == "winter":
        total_price = total_price * 0.85

charity_sum = total_price * 0.75
final_price = total_price - charity_sum
sum_per_person = final_price / count_dancers

print(f"Charity - {charity_sum:.2f}")
print(f"Money per dancer - {sum_per_person:.2f}")

