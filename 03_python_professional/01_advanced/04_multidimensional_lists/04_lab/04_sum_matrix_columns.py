rows, cols = map(int, input().split(', '))

matrix = []
for r in range(rows):
    input_nums = [int(num) for num in input().split()]
    matrix.append(input_nums)

for c in range(cols):
    column_sum = 0
    for row in matrix:
        column_sum += row[c]
    print(column_sum)
