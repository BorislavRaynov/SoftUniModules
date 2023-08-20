def movement_up(r, c):
    current_r = r + all_movements['up'][0]
    current_location = []
    direction = 'up'
    eggs_count = 0
    if 0 <= current_r < size:
        while 0 <= current_r < size:
            if isinstance(matrix[current_r][c], int):
                eggs_count += matrix[current_r][c]
                current_location.append([current_r, c])
                current_r += all_movements['up'][0]
            else:
                break
        return {eggs_count: [direction, current_location]}


def movement_down(r, c):
    current_r = r + all_movements['down'][0]
    current_location = []
    direction = 'down'
    eggs_count = 0
    if 0 <= current_r < size:
        while 0 <= current_r < size:
            if isinstance(matrix[current_r][c], int):
                eggs_count += matrix[current_r][c]
                current_location.append([current_r, c])
                current_r += all_movements['down'][0]
            else:
                break
        return {eggs_count: [direction, current_location]}


def movement_left(r, c):
    current_c = c + all_movements['left'][1]
    current_location = []
    direction = 'left'
    eggs_count = 0
    if 0 <= current_c < size:
        while 0 <= current_c < size:
            if isinstance(matrix[r][current_c], int):
                eggs_count += matrix[r][current_c]
                current_location.append([r, current_c])
                current_c += all_movements['left'][1]
            else:
                break
        return {eggs_count: [direction, current_location]}
    return {eggs_count: [direction, current_location]}


def movement_right(r, c):
    c += all_movements['right'][1]
    current_location = []
    direction = 'right'
    eggs_count = 0
    if 0 <= c < size:
        while 0 <= c < size:
            if isinstance(matrix[r][c], int):
                eggs_count += matrix[r][c]
                current_location.append([r, c])
                c += all_movements['right'][1]
            else:
                break
        return {eggs_count: [direction, current_location]}


size = int(input())

matrix = []

all_movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

bunny_location = []

for i in range(size):
    sub_str = input().split()
    current_sub = []
    for s in range(len(sub_str)):
        if sub_str[s].isdigit():
            current_sub.append(int(sub_str[s]))
        elif sub_str[s] == "B":
            bunny_location = [i, s]
            current_sub.append(sub_str[s])
        else:
            current_sub.append(sub_str[s])
    matrix.append(current_sub)

movements = {}
for key, value in movement_up(*bunny_location).items():
    if key > 0:
        movements[key] = value
for key, value in movement_down(*bunny_location).items():
    if key > 0:
        movements[key] = value
for key, value in movement_left(*bunny_location).items():
    if key > 0:
        movements[key] = value
for key, value in movement_right(*bunny_location).items():
    if key > 0:
        movements[key] = value

print(movements[max(movements)][0])
for key, value in movements.items():
    if key == max(movements):
        for v in value[1]:
            print(v)
print(max(movements))
