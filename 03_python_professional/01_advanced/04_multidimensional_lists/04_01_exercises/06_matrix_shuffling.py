rows, cols = map(int, input().split())
matrix = []
for _ in range(rows):
    matrix.append(input().split())

command = input()
while command != "END":
    command = command.split()
    count_digits = 0
    for el in command:
        if el.isdigit():
            count_digits += 1
    if command[0] == "swap" and count_digits == 4:
        invalid_input = False
        row_1 = int(command[1])
        if row_1 > rows:
            invalid_input = True
        col_1 = int(command[2])
        if col_1 > cols:
            invalid_input = True
        row_2 = int(command[3])
        if row_2 > rows:
            invalid_input = True
        col_2 = int(command[4])
        if col_2 > cols:
            invalid_input = True
        if invalid_input:
            print("Invalid input!")
            command = input()
            continue
        num_1_to_swap = matrix[row_1][col_1]
        num_2_to_swap = matrix[row_2][col_2]
        matrix[row_1][col_1] = num_2_to_swap
        matrix[row_2][col_2] = num_1_to_swap
        for element in matrix:
            print(" ".join(element))
    else:
        print("Invalid input!")
    command = input()
