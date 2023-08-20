number_companions = int(input())
number_days = int(input())
current_companions = number_companions
current_coins = 0

for day in range(1, number_days + 1):
    if day % 10 == 0:
        current_companions -= 2
    if day % 15 == 0:
        current_companions += 5
    if day % 3 == 0:
        current_coins -= current_companions * 3
    if day % 5 == 0:
        current_coins += current_companions * 20
        if day % 3 == 0:
            current_coins -= current_companions * 2
    current_coins += 50
    current_coins -= current_companions * 2

coins_per_companion = int(current_coins / current_companions)
print(f"{current_companions} companions received {coins_per_companion} coins each.")