count_total_days = int(input())

count_win = 0
count_lose = 0
days_win = 0
days_lose = 0
raised_money = 0
total_raised_money = 0

for day in range(1, count_total_days + 1):
    type_of_sport = input()
    while type_of_sport != "Finish":
        result = input()
        if result == "win":
            count_win += 1
            raised_money += 20
        else:
            count_lose += 1

        type_of_sport = input()

    if count_win > count_lose:
        raised_money = raised_money * 1.1
        total_raised_money += raised_money
        days_win += 1
    else:
        total_raised_money += raised_money
        days_lose += 1
    count_win = 0
    count_lose = 0
    raised_money = 0

if days_win > days_lose:
    total_raised_money = total_raised_money * 1.2
    print(f"You won the tournament! Total raised money: {total_raised_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_raised_money:.2f}")
