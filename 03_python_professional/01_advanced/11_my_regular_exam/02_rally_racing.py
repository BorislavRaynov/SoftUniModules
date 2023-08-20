size = int(input())
racing_number = input()

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

route = []
tunnels_coordinates = []

for x in range(size):
    row = input().split()
    for y in range(size):
        if row[y] == "T":
            tunnels_coordinates.append([x, y])
    route.append(row)

kms_passed = 0
car_has_reached_finish_line = False
disqualified = False
last_position = [0, 0]

while True:

    command = input()

    if command == "End":
        disqualified = True
        break

    last_position[0] += directions[command][0]
    last_position[1] += directions[command][1]
    r = last_position[0]
    c = last_position[1]

    if route[r][c] == "F":
        car_has_reached_finish_line = True
        kms_passed += 10
        break

    if route[r][c] == "T":
        route[r][c] = "."
        kms_passed += 30
        tunnels_coordinates.remove([r, c])
        last_position[0] = tunnels_coordinates[0][0]
        last_position[1] = tunnels_coordinates[0][1]
        route[last_position[0]][last_position[1]] = "."

    else:
        kms_passed += 10

if car_has_reached_finish_line and not disqualified:
    print(f"Racing car {racing_number} finished the stage!")

elif not car_has_reached_finish_line and disqualified:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {kms_passed} km.")
route[last_position[0]][last_position[1]] = "C"

for row in route:
    print(''.join(row))
