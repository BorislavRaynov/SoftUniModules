rows = int(input())

matrix = []

for r in range(rows):
    input_line = [int(num) for num in input().split(', ')]
    matrix.extend(input_line)

print(matrix)
