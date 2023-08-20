def check_coordinates(num1, num2):
    valid_r = num1
    valid_c = num2
    if 0 > num1:
        valid_r = rows - 1
    if rows - 1 < num1:
        valid_r = 0
    if 0 > num2:
        valid_c = cols - 1
    if cols - 1 < num2:
        valid_c = 0

    return valid_r, valid_c


rows, cols = [int(x) for x in input().split(', ')]

current_position = []
matrix = []
decorations = "D"
gifts = "G"
cookies = "C"
total_decorations = 0
total_gifts = 0
total_cookies = 0
total_items = 0
all_collected = False
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for x in range(rows):
    row = input().split()
    total_items += row.count(cookies)
    total_items += row.count(decorations)
    total_items += row.count(gifts)
    for y in range(cols):
        if row[y] == "Y":
            current_position = [x, y]
            row[y] = "x"
    matrix.append(row)

command = input()

while command != "End":
    command = command.split('-')
    direction = command[0]
    steps = int(command[1])
    for step in range(steps):
        r = current_position[0] + directions[direction][0]
        c = current_position[1] + directions[direction][1]
        current_r, current_c = check_coordinates(r, c)
        if matrix[current_r][current_c] == decorations:
            total_decorations += 1
        elif matrix[current_r][current_c] == gifts:
            total_gifts += 1
        elif matrix[current_r][current_c] == cookies:
            total_cookies += 1
        matrix[current_r][current_c] = "x"
        current_position = [current_r, current_c]
        if total_items == total_decorations + total_gifts + total_cookies:
            all_collected = True
            break

    if all_collected:
        break
    command = input()

last_r, last_c = current_position
matrix[last_r][last_c] = "Y"
if all_collected:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {total_decorations} Christmas decorations")
print(f"- {total_gifts} Gifts")
print(f"- {total_cookies} Cookies")
[print(*row) for row in matrix]
