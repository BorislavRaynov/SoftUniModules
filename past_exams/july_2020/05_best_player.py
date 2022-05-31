import sys
player_name = input()

current_goals = - sys.maxsize
current_player = ""
is_hattrick = False

while player_name != "END":
    goals = int(input())
    if goals > current_goals:
        current_goals = goals
        current_player = player_name
    if goals >= 3:
        is_hattrick = True
    if goals >= 10:
        is_hattrick = True
        break

    player_name = input()

print(f"{current_player} is the best player!")
if is_hattrick:
    print(f"He has scored {current_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {current_goals} goals.")