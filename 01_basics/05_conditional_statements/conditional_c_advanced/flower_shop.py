chrizantems_count = int(input())
roses_count = int(input())
tulips_count = int(input())
type_season = input()
holy_day = input()

total_count = roses_count + tulips_count + chrizantems_count
amount = 0

if type_season == "Spring":
    if holy_day == "Y":
        amount = (chrizantems_count * 2 + roses_count * 4.10 + tulips_count * 2.50) * 1.15
        if tulips_count >= 7:
            amount = amount * 0.95
    elif holy_day == "N":
        amount = chrizantems_count * 2 + roses_count * 4.10 + tulips_count * 2.50
        if tulips_count >= 7:
            amount = amount * 0.95
elif type_season == "Summer":
    if holy_day == "Y":
        amount = (chrizantems_count * 2 + roses_count * 4.10 + tulips_count * 2.50) * 1.15
    elif holy_day == "N":
        amount = chrizantems_count * 2 + roses_count * 4.10 + tulips_count * 2.50
elif type_season == "Winter":
    if holy_day == "Y":
        amount = (chrizantems_count * 3.75 + roses_count * 4.50 + tulips_count * 4.15) * 1.15
        if roses_count >= 10:
            amount = amount * 0.90
    elif holy_day == "N":
        amount = chrizantems_count * 3.75 + roses_count * 4.50 + tulips_count * 4.15
        if roses_count >= 10:
            amount = amount * 0.90
elif type_season == "Autumn":
    if holy_day == "Y":
        amount = (chrizantems_count * 3.75 + roses_count * 4.50 + tulips_count * 4.15) * 1.15
    elif holy_day == "N":
        amount = chrizantems_count * 3.75 + roses_count * 4.50 + tulips_count * 4.15

if total_count > 20:
    amount = amount * 0.8
    final_amount = amount + 2
    print(f"{final_amount:.2f}")
else:
    final_amount = amount + 2
    print(f"{final_amount:.2f}")