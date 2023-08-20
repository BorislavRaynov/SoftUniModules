rows = int(input())
matrix = []
for r in range(rows):
    current_nums = list(map(int, input().split(', ')))
    matrix.append([num for num in current_nums if num % 2 == 0])

print(matrix)
