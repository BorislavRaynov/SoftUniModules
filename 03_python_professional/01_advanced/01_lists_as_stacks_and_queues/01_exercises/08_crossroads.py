from collections import deque

duration_green_light = int(input())
duration_free_window = int(input())

all_cars = deque()
passed_cars = []
current_green_light = duration_green_light
current_window = duration_free_window
crash_happened = False
green_light_finish = False

command = input()
while command != "END":
    all_cars.append(command)
    command = input()

for car in all_cars:
    if car == "green":
        current_green_light = duration_green_light
        current_window = duration_free_window
        continue
    else:
        if current_green_light > len(car):
            passed_cars.append(car)
            current_green_light -= len(car)
        elif current_green_light == len(car):
            passed_cars.append(car)
            green_light_finish = True
        else:
            parts_in = car[:current_green_light:]
            left_of_the_car = car[current_green_light::]
            green_light_finish = True
            if len(left_of_the_car) <= current_window:
                passed_cars.append(car)
                current_window -= len(parts_in)
            else:
                left_of_the_car = left_of_the_car[current_window::]
                print("A crash happened!")
                print(f"{car} was hit at {left_of_the_car[0]}.")
                crash_happened = True
        if green_light_finish or crash_happened:
            break

if not crash_happened:
    print("Everyone is safe.")
    print(f"{len(passed_cars)} total cars passed the crossroads.")
