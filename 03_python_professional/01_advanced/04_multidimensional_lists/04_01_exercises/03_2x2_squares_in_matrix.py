rows, cols = map(int, input().split())
matrix = []
for r in range(rows):
    matrix.append(list(input().split()))

sub_matrix = []

for r in range(rows - 1):
    for c in range(cols - 1):
        sub_1 = [matrix[r][c], matrix[r][c + 1]]
        sub_2 = [matrix[r + 1][c], matrix[r + 1][c + 1]]
        if len(set(sub_1)) != len(set(sub_2)):
            continue
        if len(set(sub_1)) == 1:
            if sub_1 == sub_2:
                current_sub_matrix = [sub_1, sub_2]
                sub_matrix.append(current_sub_matrix)

print(len(sub_matrix))
