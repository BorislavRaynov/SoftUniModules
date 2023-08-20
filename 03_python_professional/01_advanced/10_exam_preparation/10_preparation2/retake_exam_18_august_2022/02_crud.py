matrix = [input().split() for i in range(6)]
start_position = list(map(int, input().strip("(").strip(")").split(", ")))

directions = {
    'up': (-1, 0), 'down': (1, 0),
    'left': (0, -1), 'right': (0, 1)
}

empty = '.'
command = input()
current_r = start_position[0]
current_c = start_position[1]

while command != 'Stop':
    command = command.split(', ')
    current_command = command[0]
    direction = command[1]
    current_r += directions[direction][0]
    current_c += directions[direction][1]
    current_value = matrix[current_r][current_c]

    if current_command == 'Create':
        value = command[2]
        if current_value == empty:
            matrix[current_r][current_c] = value

    elif current_command == 'Update':
        value = command[2]
        if current_value != empty:
            matrix[current_r][current_c] = value

    elif current_command == 'Delete':
        if current_value != empty:
            matrix[current_r][current_c] = empty

    elif current_command == 'Read':
        if current_value != empty:
            print(matrix[current_r][current_c])

    command = input()

for row in matrix:
    print(' '.join(row))
