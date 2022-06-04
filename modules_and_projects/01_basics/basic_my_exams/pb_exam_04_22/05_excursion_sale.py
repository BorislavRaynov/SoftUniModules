count_holiday_sea = int(input())
count_holiday_mountain = int(input())
type_bundle = input()

count_holidays = count_holiday_sea + count_holiday_mountain
current_count_sea = 0
current_count_mountain = 0
income_sea = 0
income_mountain = 0
all_holidays_are_sold = False

while type_bundle != "Stop":
    if type_bundle == "sea":
        if current_count_sea < count_holiday_sea:
            income_sea += 680
            current_count_sea += 1
            count_holidays -= 1

    elif type_bundle == "mountain":
        if current_count_mountain < count_holiday_mountain:
            income_mountain += 499
            current_count_mountain += 1
            count_holidays -= 1

    if count_holidays == 0:
        all_holidays_are_sold = True
        break
    type_bundle = input()

total_income = income_sea + income_mountain
if all_holidays_are_sold:
    print("Good job! Everything is sold.")
print(f"Profit: {total_income} leva.")
