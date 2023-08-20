size = int(input())

burrow_positions = []
snake_position = []
field = []

for x in range(size):
    line = list(input())
    for y in range(size):
        if line[y] == "B":
            burrow_positions.append([x, y])
        elif line[y] == "S":
            snake_position = [x, y]
            line[y] = "."
    field.append(line)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

food = 0
snake_go_out = False

while food < 10:
    command = input()
    snake_position[0] += directions[command][0]
    snake_position[1] += directions[command][1]
    r = snake_position[0]
    c = snake_position[1]

    if r < 0 or r > size - 1 or c < 0 or c > size - 1:
        snake_go_out = True
        break

    elif field[r][c] == "*":
        food += 1

    elif field[r][c] == "B":
        burrow_positions.remove([r, c])
        snake_position[0], snake_position[1] = burrow_positions[0][0], burrow_positions[0][1]
        field[snake_position[0]][snake_position[1]] = "."

    field[r][c] = "."

if snake_go_out:
    print("Game over!")
if food >= 10:
    print("You won! You fed the snake.")
    field[snake_position[0]][snake_position[1]] = "S"
print(f"Food eaten: {food}")
for row in field:
    print(''.join(row))
