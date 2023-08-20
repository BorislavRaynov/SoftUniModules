num = int(input())

for x in range(1, num + 1):
    print(' ' * (num - x), end='')
    for y in range(1, x + 1):
        print('* ', end='')
    print()

for i in range(num - 1, -1, -1):
    print(' ' * (num - i), end='')
    for _ in range(1, i + 1):
        print('* ', end='')
    print()
