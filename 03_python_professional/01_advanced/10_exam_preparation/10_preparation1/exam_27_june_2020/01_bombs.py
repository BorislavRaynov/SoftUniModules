from collections import deque

effects = deque(map(int, input().split(', ')))
casings = deque(map(int, input().split(', ')))

bombs_values = {'Cherry Bombs': 60, 'Datura Bombs': 40, 'Smoke Decoy Bombs': 120}
made_bombs = {'Cherry Bombs': 0, 'Datura Bombs': 0, 'Smoke Decoy Bombs': 0}

made_bomb_pouch = False

while effects and casings:

    made_bomb = False
    current_effect = effects[0]
    current_casing = casings[-1]
    current_sum = current_effect + current_casing

    for item, value in bombs_values.items():
        if value == current_sum:
            made_bombs[item] += 1
            made_bomb = True

    if made_bomb:
        effects.popleft()
        casings.pop()

    else:
        casings[-1] -= 5

    if all([value >= 3 for value in made_bombs.values()]):
        made_bomb_pouch = True
        break


if made_bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if effects:
    print(f"Bomb Effects: {', '.join(map(str, effects))}")
else:
    print("Bomb Effects: empty")
if casings:
    print(f"Bomb Casings: {', '.join(map(str, casings))}")
else:
    print("Bomb Casings: empty")
for item, value in made_bombs.items():
    print(f"{item}: {value}")
