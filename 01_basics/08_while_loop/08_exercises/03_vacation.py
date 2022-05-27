price_vacation = float(input())
init_money = float(input())

total_days = 0
count_days_spend = 0
current_money = init_money

while current_money < price_vacation:
    if count_days_spend == 5:
        too_many_days_spend = True
        break
    total_days += 1
    type_operation = input()
    amount = float(input())

    if type_operation == "spend":
        count_days_spend += 1
        current_money -= amount
        if current_money < 0:
            current_money = 0
    elif type_operation == "save":
        count_days_spend = 0
        current_money += amount

if count_days_spend == 5:
    print("You can't save the money.")
    print(total_days)
else:
    print(f"You saved the money for {total_days} days.")
