from collections import deque


def check_firework(amount):
    if amount % 15 == 0:
        return 'Crossette'
    elif amount % 5 == 0:
        return 'Willow'
    elif amount % 3 == 0:
        return 'Palm'
    return False


amount_effect = deque(x for x in map(int, input().split(', ')) if x > 0)
amount_power = deque(x for x in map(int, input().split(', ')) if x > 0)

firework_effect = {'Palm': 0, 'Willow': 0, 'Crossette': 0}
palm_made = False
willow_made = False
crossette_made = False

all_made = False

while True:
    if all_made:
        break
    elif len(amount_power) == 0:
        break
    elif len(amount_effect) == 0:
        break
    current_effect = amount_effect.popleft()
    current_power = amount_power[-1]
    current_sum = current_effect + current_power
    fire_effect = check_firework(current_sum)
    if fire_effect in firework_effect:
        firework_effect[fire_effect] += 1
        amount_power.pop()
    else:
        current_effect -= 1
        amount_effect.append(current_effect)
    if firework_effect['Palm'] >= 3:
        palm_made = True
    if firework_effect['Willow'] >= 3:
        willow_made = True
    if firework_effect['Crossette'] >= 3:
        crossette_made = True
    if palm_made and willow_made and crossette_made:
        all_made = True

if all_made:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if amount_effect:
    print(f"Firework Effects left: {', '.join(map(str, amount_effect))}")
if amount_power:
    print(f"Explosive Power left: {', '.join(map(str, amount_power))}")
for key, value in firework_effect.items():
    print(f"{key} Fireworks: {value}")
