rows, cols = map(int, input().split(', '))
matrix = []
for r in range(rows):
    matrix.append(list(map(int, input().split(', '))))

sub_matrix = []
sums_sub_matrix = []

for r in range(rows - 1):
    for c in range(cols - 1):
        sub_1 = [matrix[r][c], matrix[r][c + 1]]
        sub_2 = [matrix[r + 1][c], matrix[r + 1][c + 1]]
        current_sub_matrix = [sub_1, sub_2]
        sub_matrix.append(current_sub_matrix)
        cur_sum = sum(sub_1) + sum(sub_2)
        sums_sub_matrix.append(cur_sum)

max_sum = max(sums_sub_matrix)
searched_matrix = sub_matrix[sums_sub_matrix.index(max_sum)]
for element in searched_matrix:
    print(' '.join(list(map(str, element))))
print(max_sum)
