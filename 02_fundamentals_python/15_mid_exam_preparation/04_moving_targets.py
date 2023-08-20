targets = list(map(int, input().split()))
hit_targets = []
command = input()

while command != "End":
    split_command = command.split()
    current_command = split_command[0]
    index = int(split_command[1])
    if current_command == "Shoot":
        power = int(split_command[2])
        if 0 <= index <= len(targets) - 1:
            targets[index] -= power
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif current_command == "Add":
        value = int(split_command[2])
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif current_command == "Strike":
        radius = int(split_command[2])
        if 0 + radius <= index <= (len(targets) - 1) - radius and 1 + 2 * radius < len(targets):
            for i in range(index - radius, index + radius + 1):
                hit_targets.append(targets[i])
            for target in hit_targets:
                if target in targets:
                    targets.remove(target)
        else:
            print("Strike missed!")
    command = input()

print("|".join(list(map(str, targets))))
