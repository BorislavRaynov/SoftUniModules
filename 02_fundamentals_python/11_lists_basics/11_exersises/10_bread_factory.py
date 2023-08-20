event_list = input().replace("-", "|").split("|")
initial_energy = 100
initial_coins = 100

gained_energy = 0
gained_coins = 0
ingredient_price = 0
ingredient = ""
current_energy = initial_energy
current_coins = initial_coins
bakery_is_opened = True

for i in range(0, len(event_list), 2):
    if event_list[i] == "rest":
        temporary_energy = current_energy
        gained_energy = int(event_list[i + 1])
        current_energy += gained_energy
        if current_energy > initial_energy:
            current_energy = initial_energy
        gained_energy = current_energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif event_list[i] == "order":
        gained_coins = int(event_list[i + 1])
        if current_energy >= 30:
            current_energy -= 30
            current_coins += gained_coins
            print(f"You earned {gained_coins} coins.")
        else:
            current_energy += 50
            if current_energy > initial_energy:
                current_energy = initial_energy
            print("You had to rest!")

    else:
        ingredient = event_list[i]
        ingredient_price = int(event_list[i + 1])
        if current_coins >= ingredient_price:
            current_coins -= ingredient_price
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            bakery_is_opened = False
            break

if bakery_is_opened:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")
