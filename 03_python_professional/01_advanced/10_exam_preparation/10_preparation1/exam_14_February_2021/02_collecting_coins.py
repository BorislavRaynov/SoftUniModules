from math import floor

size = int(input())

starting_coordinates = []
my_coordinates = []
matrix = []
total_points = 0
hits_a_wall = False
directions ={
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for x in range(size):
    input_line = input().split()
    row = []
    for y in range(size):
        if input_line[y].isdigit():
            row.append(int(input_line[y]))
        else:
            if input_line[y] == "P":
                starting_coordinates = [x, y]
                my_coordinates.append([x, y])
            row.append(input_line[y])
    matrix.append(row)

matrix[starting_coordinates[0]][starting_coordinates[1]] = 0

while total_points < 100:
    direction = input()
    if direction in directions:
        starting_coordinates[0] += directions[direction][0]
        starting_coordinates[1] += directions[direction][1]
        if starting_coordinates[0] < 0:
            starting_coordinates[0] = size - 1
        if starting_coordinates[0] > size - 1:
            starting_coordinates[0] = 0
        if starting_coordinates[1] < 0:
            starting_coordinates[1] = size - 1
        if starting_coordinates[1] > size - 1:
            starting_coordinates[1] = 0
        if matrix[starting_coordinates[0]][starting_coordinates[1]] == "X":
            hits_a_wall = True
            my_coordinates.append([starting_coordinates[0], starting_coordinates[1]])
            break
        else:
            last_r = starting_coordinates[0]
            last_c = starting_coordinates[1]
            total_points += matrix[starting_coordinates[0]][starting_coordinates[1]]
            matrix[starting_coordinates[0]][starting_coordinates[1]] = 0
            my_coordinates.append([last_r, last_c])

if total_points >= 100:
    print(f"You won! You've collected {total_points} coins.")
else:
    total_points = floor(total_points / 2)
    print(f"Game over! You've collected {total_points} coins.")
print('Your path:')
for coordinate in my_coordinates:
    print(coordinate)