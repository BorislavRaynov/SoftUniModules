def move_up(string, r, c):
    current_presents = 0
    current_nice_kids = 0

    if 0 <= r + movements[string][0] < size:
        r = r + movements[string][0]
        if field[r][c] == nice_kid:
            current_presents += 1
            current_nice_kids += 1

        elif field[r][c] == cookie:
            total_given = 0
            if field[r + 1][c] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r - 1][c] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r][c + 1] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r][c - 1] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r + 1][c] == naughty_kid:
                total_given += 1
            if field[r - 1][c] == naughty_kid:
                total_given += 1
            if field[r][c + 1] == naughty_kid:
                total_given += 1
            if field[r][c - 1] == naughty_kid:
                total_given += 1
            current_presents += total_given
    return [r, c, current_presents, current_nice_kids]


def move_left(string, r, c):
    current_presents = 0
    current_nice_kids = 0

    if 0 <= c + movements[string][1] < size:
        c = c + movements[string][1]
        if field[r][c] == nice_kid:
            current_presents += 1
            current_nice_kids += 1

        elif field[r][c] == cookie:
            total_given = 0
            if field[r + 1][c] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r - 1][c] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r][c + 1] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r][c - 1] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r + 1][c] == naughty_kid:
                total_given += 1
            if field[r - 1][c] == naughty_kid:
                total_given += 1
            if field[r][c + 1] == naughty_kid:
                total_given += 1
            if field[r][c - 1] == naughty_kid:
                total_given += 1
            current_presents += total_given
    return [r, c, current_presents, current_nice_kids]


def move_down(string, r, c):
    current_presents = 0
    current_nice_kids = 0

    if 0 <= r + movements[string][0] < size:
        r = r + movements[string][0]
        if field[r][c] == nice_kid:
            current_presents += 1
            current_nice_kids += 1

        elif field[r][c] == cookie:
            total_given = 0
            if field[r + 1][c] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r - 1][c] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r][c + 1] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r][c - 1] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r + 1][c] == naughty_kid:
                total_given += 1
            if field[r - 1][c] == naughty_kid:
                total_given += 1
            if field[r][c + 1] == naughty_kid:
                total_given += 1
            if field[r][c - 1] == naughty_kid:
                total_given += 1
            current_presents += total_given
    return [r, c, current_presents, current_nice_kids]


def move_right(string, r, c):
    current_presents = 0
    current_nice_kids = 0

    if 0 <= c + movements[string][1] < size:
        c = c + movements[string][1]
        if field[r][c] == nice_kid:
            current_presents += 1
            current_nice_kids += 1

        elif field[r][c] == cookie:
            total_given = 0
            if field[r + 1][c] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r - 1][c] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r][c + 1] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r][c - 1] == nice_kid:
                current_nice_kids += 1
                total_given += 1
            if field[r + 1][c] == naughty_kid:
                total_given += 1
            if field[r - 1][c] == naughty_kid:
                total_given += 1
            if field[r][c + 1] == naughty_kid:
                total_given += 1
            if field[r][c - 1] == naughty_kid:
                total_given += 1
            current_presents += total_given
    return [r, c, current_presents, current_nice_kids]


presents = int(input())
size = int(input())

naughty_kid = "X"
nice_kid = "V"
cookie = "C"
empty = "-"
all_nice_kids = 0
nice_kids_count = 0
santa_r, santa_c = 0, 0
field = []

for i in range(size):
    line = input().split()
    nice_kids_count += line.count(nice_kid)
    all_nice_kids += line.count(nice_kid)
    field.append(line)
    for _ in range(len(line)):
        if line[_] == "S":
            santa_r, santa_c = i, _
            line[_] = empty

movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

command = input()
while True:

    if command == "Christmas morning":
        break

    if command == "up":
        result = move_up(command, santa_r, santa_c)
        santa_r, santa_c = result[0], result[1]
        field[santa_r][santa_c] = empty
        presents -= result[2]
        nice_kids_count -= result[3]

    elif command == "down":
        result = move_down(command, santa_r, santa_c)
        santa_r, santa_c = result[0], result[1]
        field[santa_r][santa_c] = empty
        presents -= result[2]
        nice_kids_count -= result[3]

    elif command == "left":
        result = move_left(command, santa_r, santa_c)
        santa_r, santa_c = result[0], result[1]
        field[santa_r][santa_c] = empty
        presents -= result[2]
        nice_kids_count -= result[3]

    elif command == "right":
        result = move_right(command, santa_r, santa_c)
        santa_r, santa_c = result[0], result[1]
        field[santa_r][santa_c] = empty
        presents -= result[2]
        nice_kids_count -= result[3]

    if presents == 0:
        break

    command = input()

if presents <= 0 and nice_kids_count > 0:
    print("Santa ran out of presents!")
field[santa_r][santa_c] = "S"
[print(" ".join(i)) for i in field]
if nice_kids_count <= 0:
    print(f"Good job, Santa! {all_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count} nice kid/s.")
