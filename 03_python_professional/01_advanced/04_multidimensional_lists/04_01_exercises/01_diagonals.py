size = int(input())
primary_diagonal = []
secondary_diagonal = []
matrix = []

for _ in range(size):
    matrix.append(list(map(int, input().split(', '))))

for r in range(size):
    primary_diagonal.append(matrix[r][r])

limit = size - 1
for i in range(size):
    secondary_diagonal.append(matrix[i][limit])
    limit -= 1

print(f"Primary diagonal: {', '.join(list(map(str, primary_diagonal)))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(list(map(str, secondary_diagonal)))}. Sum: {sum(secondary_diagonal)}")
