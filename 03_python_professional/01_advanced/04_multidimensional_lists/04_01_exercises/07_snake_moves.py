rows, cols = [int(x) for x in input().split()]
snake = input()
matrix = []
idx = 0
for row in range(rows):
    result = ""
    for col in range(cols):
        result += snake[idx % len(snake)]
        idx += 1

    if row % 2 == 0:
        matrix.append(result)
    else:
        matrix.append(result[::-1])

for sub in matrix:
    print(*sub, sep='')
