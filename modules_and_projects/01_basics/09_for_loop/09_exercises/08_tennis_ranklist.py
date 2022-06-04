from math import floor
count_tournaments = int(input())
init_points = int(input())

total_points = init_points
win_tournaments = 0
for i in range(1, count_tournaments + 1):
    position = input()
    if position == "W":
        total_points += 2000
        win_tournaments += 1
    elif position == "F":
        total_points += 1200
    elif position == "SF":
        total_points += 720

average_points = (total_points - init_points) / count_tournaments
win_percent = (win_tournaments / count_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_percent:.2f}%")