goal_steps = 10000

command = input()

total_steps = 0
has_reached_goal = False

while total_steps < goal_steps:
    if command == "Going home":
        steps_after = int(input())
        total_steps += steps_after
        if total_steps >= goal_steps:
            has_reached_goal = True
        break
    else:
        total_steps += int(command)
        if total_steps >= goal_steps:
            has_reached_goal = True
            break
    command = input()

diff = abs(total_steps - goal_steps)
if has_reached_goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
