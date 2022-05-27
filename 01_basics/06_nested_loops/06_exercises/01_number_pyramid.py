num = int(input())

current_n = 1
for row in range(1, num + 1):
    for col in range(1, row + 1):
        if current_n > num:
            break
        print(current_n, end=" ")
        current_n += 1
    if current_n > num:
        break
    print()