from collections import deque

caffeine = deque(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))
max_caffeine = 300
initial_amount = 0

while caffeine and energy_drinks:

    current_caffeine = caffeine[-1]
    current_drink = energy_drinks[0]
    current_result = current_caffeine * current_drink

    if current_result + initial_amount <= max_caffeine:
        initial_amount += current_result
        caffeine.pop()
        energy_drinks.popleft()

    else:
        caffeine.pop()
        energy_drinks.append(energy_drinks.popleft())
        initial_amount -= 30
        if initial_amount < 0:
            initial_amount = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {initial_amount} mg caffeine.")
