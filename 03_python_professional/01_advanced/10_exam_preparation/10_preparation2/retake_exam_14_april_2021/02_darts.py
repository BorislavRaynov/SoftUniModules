from collections import deque
from math import ceil


def player_win(name, points):
    if points <= 0:
        return name


size = 7

players = deque(input().split(', '))
dart_board = [input().split() for i in range(size)]

current_points = {players[0]: 501,  players[1]: 501}
winner = ''
turn = 0

while True:
    trow = input().strip('(').strip(')').split(', ')
    r = int(trow[0])
    c = int(trow[1])
    current_player = players[0]
    turn += 1
    if r < 0 or r > size - 1 or c < 0 or c > size - 1:
        players.append(players.popleft())
        continue

    elif dart_board[r][c] == "B":
        winner = current_player

    elif dart_board[r][c].isdigit():
        current_points[current_player] -= int(dart_board[r][c])
        winner = player_win(current_player, current_points[current_player])

    elif dart_board[r][c].isalpha():
        points_from_trow = int(dart_board[0][c]) + int(dart_board[r][0]) + int(dart_board[6][c]) + int(dart_board[r][6])
        if dart_board[r][c] == "D":
            current_points[current_player] -= points_from_trow * 2
        elif dart_board[r][c] == "T":
            current_points[current_player] -= points_from_trow * 3
        winner = player_win(current_player, current_points[current_player])

    if winner:
        break
    else:
        players.append(players.popleft())

print(f"{winner} won the game with {ceil(turn / 2)} throws!")
