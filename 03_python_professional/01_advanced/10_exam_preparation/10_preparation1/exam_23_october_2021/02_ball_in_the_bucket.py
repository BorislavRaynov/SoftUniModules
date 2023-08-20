def check_won_prize(points, prizes):
    for key, value in prizes.items():
        if value[0] <= points <= value[1]:
            return key
    return False


size = 6

board = [input().split() for i in range(size)]
rewards = {
    'Football': [100, 199],
    'Teddy Bear': [200, 299],
    'Lego Construction Set': [300, 10000]
}

columns_collected = []
collected_points = 0

for trow in range(3):
    current_coordinates = input().strip("(").strip(")").split(", ")
    current_r = int(current_coordinates[0])
    current_c = int(current_coordinates[1])
    if 0 <= current_r < size and 0 <= current_c < size:
        if board[current_r][current_c] == "B":
            if current_c not in columns_collected:
                for i in range(size):
                    if board[i][current_c].isdigit():
                        collected_points += int(board[i][current_c])
                columns_collected.append(current_c)

prize = check_won_prize(collected_points, rewards)
if prize:
    print(f"Good job! You scored {collected_points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - collected_points} points more to win a prize.")
