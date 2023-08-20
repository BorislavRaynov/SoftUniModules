number_days = int(input())
plunder_per_day = int(input())
target_plunder = float(input())

current_plunder = 0

for day in range(1, number_days + 1):
    current_plunder += plunder_per_day
    if day % 3 == 0:
        current_plunder += plunder_per_day * 0.5
    if day % 5 == 0:
        current_plunder *= 0.7
if current_plunder >= target_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    percentage = (current_plunder / target_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
