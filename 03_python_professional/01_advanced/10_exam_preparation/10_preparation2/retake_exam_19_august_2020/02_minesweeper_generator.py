SIZE = int(input())
count_bombs = int(input())
coordinates_of_bombs = []
field = [[0] * SIZE for i in range(SIZE)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

for i in range(count_bombs):
    coordinate = input().strip("()").split(', ')
    r = int(coordinate[0])
    c = int(coordinate[1])
    if r < 0 or r > SIZE - 1 or c < 0 or c > SIZE - 1:
        continue
    field[r][c] = '*'

for x in range(SIZE):
    for y in range(SIZE):
        if field[x][y] == "*":
            for direction in directions:
                current_r = x + direction[0]
                current_c = y + direction[1]
                if current_r < 0 or current_r > SIZE - 1 or current_c < 0 or current_c > SIZE - 1:
                    continue
                elif field[current_r][current_c] == "*":
                    continue
                else:
                    field[current_r][current_c] += 1

for row in field:
    print(' '.join(map(str, row)))
