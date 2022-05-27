change_back = float(input())

change_left_cents = round(change_back * 100)
total_coins = 0

while change_left_cents > 0:
    if change_left_cents >= 200:
        change_left_cents -= 200
        total_coins += 1
    elif change_left_cents >= 100:
        change_left_cents -= 100
        total_coins += 1
    elif change_left_cents >= 50:
        change_left_cents -= 50
        total_coins += 1
    elif change_left_cents >= 20:
        change_left_cents -= 20
        total_coins += 1
    elif change_left_cents >= 10:
        change_left_cents -= 10
        total_coins += 1
    elif change_left_cents >= 5:
        change_left_cents -= 5
        total_coins += 1
    elif change_left_cents >= 2:
        change_left_cents -= 2
        total_coins += 1
    elif change_left_cents >= 1:
        change_left_cents -= 1
        total_coins += 1

print(f"{total_coins}")
