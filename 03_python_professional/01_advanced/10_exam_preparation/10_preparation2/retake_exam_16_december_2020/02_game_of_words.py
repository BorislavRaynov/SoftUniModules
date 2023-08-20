initial_string = input()
size = int(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

starting_position = []
field = []

for x in range(size):
    row = list(input())
    for y in range(len(row)):
        if row[y] == "P":
            starting_position = [x, y]
            row[y] = '-'
    field.append(row)

count_commands = int(input())
for com in range(count_commands):
    command = input()
    r = directions[command][0] + starting_position[0]
    c = directions[command][1] + starting_position[1]
    if r < 0 or r > size - 1 or c < 0 or c > size - 1:
        if initial_string:
            initial_string = initial_string[:-1:]
        continue
    if field[r][c] == '-':
        starting_position[0] = r
        starting_position[1] = c
        continue
    if field[r][c].isalpha():
        initial_string += field[r][c]
        field[r][c] = '-'
        starting_position[0] = r
        starting_position[1] = c
        continue

field[starting_position[0]][starting_position[1]] = 'P'
print(initial_string)
for row in field:
    print(''.join(row))
