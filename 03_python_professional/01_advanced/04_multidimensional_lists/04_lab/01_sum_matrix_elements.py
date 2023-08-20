data = list(map(int, input().split(', ')))
rows, cols = data[0], data[1]

matrix = []
matrix_sum = 0
for r in range(rows):
    current_row = list(map(int, input().split(', ')))
    matrix_sum += sum(current_row)
    matrix.append(current_row)
print(matrix_sum)
print(matrix)