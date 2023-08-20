track = list(map(int, input().split()))
middle = int((len(track) + 1) / 2)

left_car_time = []
right_car_time = []
total_left_car = 0
total_right_car = 0

left_car_time += track[:middle - 1]
right_car_time += track[-1:middle - 1: - 1]

for time in left_car_time:
    total_left_car += time
    if time == 0:
        total_left_car *= 0.8

for time in right_car_time:
    total_right_car += time
    if time == 0:
        total_right_car *= 0.8


if total_left_car < total_right_car:
    print(f"The winner is left with total time: {total_left_car:.1f}")
else:
    print(f"The winner is right with total time: {total_right_car:.1f}")

