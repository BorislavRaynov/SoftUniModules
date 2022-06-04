from math import floor
count_balls = int(input())

count_red = 0
count_orange = 0
count_yellow = 0
count_white = 0
count_black = 0
count_others = 0
current_points = 0

for ball in range(1, count_balls + 1):
    colour = input()
    if colour == "red":
        count_red += 1
        current_points += 5
    elif colour == "orange":
        count_orange += 1
        current_points += 10
    elif colour == "yellow":
        count_yellow += 1
        current_points += 15
    elif colour == "white":
        count_white += 1
        current_points += 20
    elif colour == "black":
        count_black += 1
        current_points = floor(current_points / 2)
    else:
        count_others += 1

print(f"Total points: {current_points}")
print(f"Red balls: {count_red}")
print(f"Orange balls: {count_orange}")
print(f"Yellow balls: {count_yellow}")
print(f"White balls: {count_white}")
print(f"Other colors picked: {count_others}")
print(f"Divides from black balls: {count_black}")
