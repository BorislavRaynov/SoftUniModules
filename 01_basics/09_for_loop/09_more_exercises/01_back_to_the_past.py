init_money = float(input())
year_goal = int(input())

money_spend = 0

for i in range(1800, year_goal + 1):
    if i % 2 == 0:
        money_spend += 12000
    else:
        money_spend += 12000 + ((i + 18 - 1800) * 50)

diff = abs(init_money - money_spend)
if init_money >= money_spend:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")