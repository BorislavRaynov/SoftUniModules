actor_name = input()
init_points = float(input())
count_jury = int(input())

total_points = init_points

for jury in range(1, count_jury + 1):
    jury_name = input()
    jury_init_points = float(input())
    jury_points = (len(jury_name) * jury_init_points) / 2
    total_points += jury_points
    if total_points >= 1250.5:
        break

if total_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = abs(total_points - 1250.5)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")