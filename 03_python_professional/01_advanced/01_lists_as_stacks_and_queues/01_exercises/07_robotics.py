from collections import deque
from time import strftime
from time import gmtime


def setting_correct_time(seconds):
    time_to_be_printed = strftime("%H:%M:%S", gmtime(seconds))
    return f"[{time_to_be_printed}]"


robots = input().split(";")
time = list(map(int, input().split(":")))
starting_time = time[0] * 3600 + time[1] * 60 + time[2]
total_time = starting_time

robots_info = {}
products = deque()

for robot in robots:
    name, sec = robot.split("-")
    robots_info[name] = int(sec)

busy_robots = {x: 0 for x in robots_info.keys()}
product = input()
while product != "End":
    products.append(product)
    product = input()

while products:
    total_time += 1
    current_product = products.popleft()

    for robot, busy_until in busy_robots.items():
        if total_time >= busy_until:
            busy_robots[robot] = total_time + robots_info[robot]
            print(f"{robot} - {current_product} {setting_correct_time(total_time)}")
            break

    else:
        products.append(current_product)
