initial_energy = int(input())

current_energy = initial_energy
won_battles = 0

while True:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {current_energy}")
        break
    energy_to_reach_enemy = int(distance)
    if current_energy < energy_to_reach_enemy:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {current_energy} energy")
        break
    if current_energy >= energy_to_reach_enemy:
        won_battles += 1
        current_energy -= energy_to_reach_enemy
        if won_battles % 3 == 0:
            current_energy += won_battles

