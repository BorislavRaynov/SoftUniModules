size = int(input())

matrix = []
alice_row = 0
alice_col = 0

for _ in range(size):
    line = input().split()
    for i in range(len(line)):
        if line[i] == "A":
            alice_row = _
            alice_col = i
    matrix.append(line)

matrix[alice_row][alice_col] = "*"
collected_tea_bags = 0
alice_collect_all = False
alice_not_made_it = False

while True:
    if collected_tea_bags >= 10:
        alice_collect_all = True
        break
    command = input()
    if command == "up":
        alice_new_row = alice_row - 1
        if alice_new_row < 0:
            alice_not_made_it = True
            break
        elif matrix[alice_new_row][alice_col] == "R":
            matrix[alice_new_row][alice_col] = "*"
            alice_not_made_it = True
            break
        elif matrix[alice_new_row][alice_col].isdigit():
            collected_tea_bags += int(matrix[alice_new_row][alice_col])
        matrix[alice_new_row][alice_col] = "*"
        alice_row = alice_new_row
    elif command == "down":
        alice_new_row = alice_row + 1
        if alice_new_row > size - 1:
            alice_not_made_it = True
            break
        elif matrix[alice_new_row][alice_col] == "R":
            matrix[alice_new_row][alice_col] = "*"
            alice_not_made_it = True
            break
        elif matrix[alice_new_row][alice_col].isdigit():
            collected_tea_bags += int(matrix[alice_new_row][alice_col])
        matrix[alice_new_row][alice_col] = "*"
        alice_row = alice_new_row
    elif command == "left":
        alice_new_col = alice_col - 1
        if alice_new_col < 0:
            alice_not_made_it = True
            break
        elif matrix[alice_row][alice_new_col] == "R":
            matrix[alice_row][alice_new_col] = "*"
            alice_not_made_it = True
            break
        elif matrix[alice_row][alice_new_col].isdigit():
            collected_tea_bags += int(matrix[alice_row][alice_new_col])
        matrix[alice_row][alice_new_col] = "*"
        alice_col = alice_new_col
    elif command == "right":
        alice_new_col = alice_col + 1
        if alice_new_col > size - 1:
            alice_not_made_it = True
            break
        elif matrix[alice_row][alice_new_col] == "R":
            matrix[alice_row][alice_new_col] = "*"
            alice_not_made_it = True
            break
        elif matrix[alice_row][alice_new_col].isdigit():
            collected_tea_bags += int(matrix[alice_row][alice_new_col])
        matrix[alice_row][alice_new_col] = "*"
        alice_col = alice_new_col

if alice_collect_all:
    print("She did it! She went to the party.")
elif alice_not_made_it:
    print("Alice didn't make it to the tea party.")

[print(" ".join(line)) for line in matrix]
