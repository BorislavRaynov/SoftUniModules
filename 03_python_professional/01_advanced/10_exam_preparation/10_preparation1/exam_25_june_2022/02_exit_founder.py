from collections import deque

names = deque(input().split(', '))

size = 6
exit_symbol = "E"
trap = "T"
wall = "W"
empty = "."
skipping = {"Tom": 0, "Jerry": 0}

matrix = [input().split() for i in range(size)]

while True:

    coordinates_as_str = input().strip('(').strip(')').split(', ')
    r = int(coordinates_as_str[0])
    c = int(coordinates_as_str[1])
    position = matrix[r][c]
    current_player = names[0]

    if skipping[current_player] > 0:
        skipping[current_player] -= 1

    elif position == wall:
        print(f"{current_player} hits a wall and needs to rest.")
        skipping[current_player] += 1

    elif matrix[r][c] == exit_symbol:
        print(f"{current_player} found the Exit and wins the game!")
        break

    elif matrix[r][c] == trap:
        print(f"{current_player} is out of the game! The winner is {names[-1]}.")
        break

    names.append(names.popleft())
