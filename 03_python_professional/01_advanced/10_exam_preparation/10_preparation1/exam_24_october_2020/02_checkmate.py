def movement(starting_r, starting_c, step_r, step_c):
    r = starting_r
    c = starting_c
    while True:
        r += step_r
        c += step_c
        if r < 0 or r > size - 1 or c < 0 or c > size - 1:
            return False
        elif board[r][c] == queen:
            return [r, c]


size = 8
board = []
king_coord = []
valid_queens = []
queen = 'Q'
king_is_safe = True

for x in range(size):
    row = input().split()
    for y in range(size):
        if row[y] == 'K':
            king_coord = [x, y]
    board.append(row)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'up_left': (-1, -1),
    'up_right': (-1, 1),
    'down_left': (1, -1),
    'down_right': (1, 1)
}

for direction in directions:
    result_coordinates = movement(*king_coord, *directions[direction])
    if result_coordinates:
        valid_queens.append(result_coordinates)
        king_is_safe = False

if king_is_safe:
    print('The king is safe!')
else:
    for q in valid_queens:
        print(q)
