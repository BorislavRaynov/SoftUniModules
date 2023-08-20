rows, cols = map(int, input().split())
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

sub_matrix = []
sums_sub_matrix = []

for r in range(rows - 2):
    for c in range(cols - 2):
        sub_1 = [matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]]
        sub_2 = [matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]]
        sub_3 = [matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]]
        current_sub_matrix = [sub_1, sub_2, sub_3]
        sub_matrix.append(current_sub_matrix)
        cur_sum = sum(sub_1) + sum(sub_2) + sum(sub_3)
        sums_sub_matrix.append(cur_sum)

max_sum = max(sums_sub_matrix)
searched_matrix = sub_matrix[sums_sub_matrix.index(max_sum)]
print(f"Sum = {max_sum}")
for element in searched_matrix:
    print(' '.join(list(map(str, element))))
