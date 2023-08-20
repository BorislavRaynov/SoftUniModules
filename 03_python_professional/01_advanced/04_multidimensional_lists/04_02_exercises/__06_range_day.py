size = 5
target = "x"

field = []
current_row = 0
current_col = 0
count_targets = 0
all_targets = 0
for i in range(size):
    line = input().split()
    for s in range(len(line)):
        if line[s] == "A":
            current_row = i
            current_col = s
        elif line[s] == target:
            count_targets += 1
            all_targets += 1
    field.append(line)

field[current_row][current_col] = "."

command_count = int(input())
training_complete = False
targets_shot = []
for com in range(command_count):
    command = input().split()
    to_do = command[0]
    direction = command[1]
    if to_do == "move":
        steps = int(command[2])
        if direction == "up":
            new_row = current_row - steps
            if new_row < 0:
                continue
            else:
                count_steps = 0
                for step in range(current_row - 1, new_row - 1, -1):
                    if field[step][current_col] == ".":
                        count_steps += 1
                if count_steps == steps:
                    current_row = new_row

        elif direction == "down":
            new_row = current_row + steps
            if new_row > size - 1:
                continue
            else:
                count_steps = 0
                for step in range(current_row + 1, new_row + 1):
                    if field[step][current_col] == ".":
                        count_steps += 1
                if count_steps == steps:
                    current_row = new_row
        elif direction == "right":
            new_col = current_col + steps
            if new_col > size - 1:
                continue
            else:
                count_steps = 0
                for step in range(current_col + 1, new_col + 1):
                    if field[current_row][step] == ".":
                        count_steps += 1
                if count_steps == steps:
                    current_col = new_col
        elif direction == "left":
            new_col = current_col - steps
            if new_col < 0:
                continue
            else:
                count_steps = 0
                for step in range(current_col - 1, new_col - 1, - 1):
                    if field[current_row][step] == ".":
                        count_steps += 1
                if count_steps == steps:
                    current_col = new_col
    elif to_do == "shoot":
        if direction == "up":
            if current_row > 0:
                for r in range(current_row - 1, - 1, - 1):
                    if field[r][current_col] == target:
                        field[r][current_col] = "."
                        targets_shot.append([r, current_col])
                        count_targets -= 1
                        break
        elif direction == "down":
            if current_row < size - 1:
                for r in range(current_row + 1, size):
                    if field[r][current_col] == target:
                        field[r][current_col] = "."
                        targets_shot.append([r, current_col])
                        count_targets -= 1
                        break
        elif direction == "right":
            if current_col < size - 1:
                for c in range(current_col + 1, size):
                    if field[current_row][c] == target:
                        field[current_row][c] = "."
                        targets_shot.append([current_row, c])
                        count_targets -= 1
                        break
        elif direction == "left":
            if current_col > 0:
                for c in range(current_col - 1, -1, -1):
                    if field[current_row][c] == target:
                        field[current_row][c] = "."
                        targets_shot.append([current_row, c])
                        count_targets -= 1
                        break
        if count_targets == 0:
            training_complete = True
            break

if training_complete:
    print(f"Training completed! All {all_targets} targets hit.")
else:
    print(f"Training not completed! {count_targets} targets left.")
for position in targets_shot:
    print(position)
