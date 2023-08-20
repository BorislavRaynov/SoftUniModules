size = int(input())

matrix = []

for r in range(size):
    matrix.append([int(n) for n in input().split()])
diagonal_sum = 0
for i in range(size):
    for c in range(size):
        if i == c:
            diagonal_sum += matrix[i][i]

print(diagonal_sum)
