first_line = list(map(int, input().split()))
second_line = list(map(int, input().split()))
third_line = list(map(int, input().split()))

first_player_won = False
second_player_won = False

if first_line[0] == 1 and first_line[1] == 1 and first_line[2] == 1:
    first_player_won = True
elif first_line[0] == 1 and second_line[0] == 1 and third_line[0] == 1:
    first_player_won = True
elif first_line[0] == 1 and second_line[1] == 1 and third_line[2] == 1:
    first_player_won = True
elif first_line[1] == 1 and second_line[1] == 1 and third_line[1] == 1:
    first_player_won = True
elif first_line[2] == 1 and second_line[2] == 1 and third_line[2] == 1:
    first_player_won = True
elif first_line[2] == 1 and second_line[1] == 1 and third_line[0] == 1:
    first_player_won = True
elif second_line[0] == 1 and second_line[1] == 1 and second_line[2] == 1:
    first_player_won = True
elif third_line[0] == 1 and third_line[1] == 1 and third_line[2] == 1:
    first_player_won = True
elif first_line[0] == 2 and first_line[1] == 2 and first_line[2] == 2:
    second_player_won = True
elif first_line[0] == 2 and second_line[0] == 2 and third_line[0] == 2:
    second_player_won = True
elif first_line[0] == 2 and second_line[1] == 2 and third_line[2] == 2:
    second_player_won = True
elif first_line[1] == 2 and second_line[1] == 2 and third_line[1] == 2:
    second_player_won = True
elif first_line[2] == 2 and second_line[2] == 2 and third_line[2] == 2:
    second_player_won = True
elif first_line[2] == 2 and second_line[1] == 2 and third_line[0] == 2:
    second_player_won = True
elif second_line[0] == 2 and second_line[1] == 2 and second_line[2] == 2:
    second_player_won = True
elif third_line[0] == 2 and third_line[1] == 2 and third_line[2] == 2:
    second_player_won = True

if first_player_won:
    print("First player won")
elif second_player_won:
    print("Second player won")
else:
    print("Draw!")