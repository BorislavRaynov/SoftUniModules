from collections import deque

size = 6
rover = "E"
water = "W"
metal = "M"
concrete = "C"
rock = "R"
empty = "-"

directions = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
rover_coord = []
field = []

for x in range(size):
    row = input().split()
    for y in range(len(row)):
        if row[y] == rover:
            rover_coord = [x, y]
    field.append(row)

commands = deque(input().split(', '))

rover_is_broken = False
found_water = False
found_metal = False
found_concrete = False

r, c = rover_coord
value_rover = 0

while commands:
    current_command = commands.popleft()
    r += directions[current_command][0]
    c += directions[current_command][1]

    if r > size - 1:
        r = 0
    if c > size - 1:
        c = 0
    if r < 0:
        r = size - 1
    if c < 0:
        c = size - 1

    if field[r][c] == rock:
        rover_is_broken = True
        print(f"Rover got broken at ({r}, {c})")
        break
    elif field[r][c] == water:
        print(f"Water deposit found at ({r}, {c})")
        found_water = True
        value_rover += 1
    elif field[r][c] == metal:
        print(f"Metal deposit found at ({r}, {c})")
        found_metal = True
        value_rover += 1
    elif field[r][c] == concrete:
        print(f"Concrete deposit found at ({r}, {c})")
        found_concrete = True
        value_rover += 1

if found_water and found_metal and found_concrete:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
