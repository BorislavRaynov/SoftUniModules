size = int(input())

field = [list(input())for i in range(size)]

movements = [
    (-2, 1), (-2, -1), (-1, -2), (-1, 2),
    (2, 1), (2, -1), (1, 2), (1, -2)
]

knights_removed_count = 0

while True:
    max_attacks = 0
    knight_most_attacks = []

    for r in range(size):
        for c in range(size):
            if field[r][c] == "K":
                current_attacks = 0
                for move in movements:
                    searched_r, searched_c = r + move[0], c + move[1]
                    if 0 <= searched_r < size and 0 <= searched_c < size:
                        if field[searched_r][searched_c] == "K":
                            current_attacks += 1
                if current_attacks > max_attacks:
                    max_attacks = current_attacks
                    knight_most_attacks = [r, c]

    if knight_most_attacks:
        field[knight_most_attacks[0]][knight_most_attacks[1]] = "0"
        knights_removed_count += 1
    else:
        break

print(knights_removed_count)


