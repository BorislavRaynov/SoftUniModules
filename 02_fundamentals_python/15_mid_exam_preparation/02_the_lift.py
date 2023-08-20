people_waiting = int(input())
current_state_lift = list(map(int, input(). split()))

current_people_waiting = people_waiting
wagon_max_size = 4

for wagon in range(len(current_state_lift)):

    if current_people_waiting > 3:
        current_people_waiting -= wagon_max_size - current_state_lift[wagon]
        current_state_lift[wagon] = wagon_max_size

    else:
        current_state_lift[wagon] += current_people_waiting
        current_people_waiting = 0

if current_people_waiting > 0:
    print(f"There isn't enough space! {current_people_waiting} people in a queue!")
elif sum(current_state_lift) != len(current_state_lift) * wagon_max_size:
    print("The lift has empty spots!")

print(" ".join(map(str, current_state_lift)))
