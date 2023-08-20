budget = float(input())
category = input()
count_people = int(input())

vip_price = 499.99
normal_price = 249.99
expenses = 0

if category == "VIP":
    if 1 <= count_people <= 4:
        expenses = count_people * vip_price + budget * 0.75
    elif 5 <= count_people <= 9:
        expenses = count_people * vip_price + budget * 0.6
    elif 10 <= count_people <= 24:
        expenses = count_people * vip_price + budget * 0.5
    elif 25 <= count_people <= 49:
        expenses = count_people * vip_price + budget * 0.4
    elif count_people >= 50:
        expenses = count_people * vip_price + budget * 0.25
elif category == "Normal":
    if 1 <= count_people <= 4:
        expenses = count_people * normal_price + budget * 0.75
    elif 5 <= count_people <= 9:
        expenses = count_people * normal_price + budget * 0.6
    elif 10 <= count_people <= 24:
        expenses = count_people * normal_price + budget * 0.5
    elif 25 <= count_people <= 49:
        expenses = count_people * normal_price + budget * 0.4
    elif count_people >= 50:
        expenses = count_people * normal_price + budget * 0.25

diff = abs(budget - expenses)
if budget >= expenses:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")