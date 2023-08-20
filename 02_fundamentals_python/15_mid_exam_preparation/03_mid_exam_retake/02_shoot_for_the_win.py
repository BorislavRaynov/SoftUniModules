targets = list(map(int, input(). split()))
indices = input()
shot_targets_indices = []
count_shot_targets = 0

while indices != "End":
    current_index = int(indices)
    if current_index <= len(targets) - 1 and targets[current_index] != -1:
        count_shot_targets += 1
        current_target_value = targets[current_index]
        targets[current_index] = -1
        for target in range(len(targets)):
            if targets[target] > current_target_value and targets[target] != -1:
                targets[target] -= current_target_value
            elif targets[target] <= current_target_value and targets[target] != -1:
                targets[target] += current_target_value

    indices = input()
current_state_of_targets = list(map(str, targets))
print(f"Shot targets: {count_shot_targets} -> {' '.join(current_state_of_targets)}")
