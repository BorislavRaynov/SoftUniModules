stack = []
num = int(input())

for queries in range(num):
    query = list(map(int, input().split()))
    current_num = query[0]
    if current_num == 1:
        stack.append(query[1])
    elif current_num == 2:
        if stack:
            stack.pop()
    elif current_num == 3:
        if stack:
            print(max(stack))
    elif current_num == 4:
        if stack:
            print(min(stack))

print(", ".join(map(str, stack[::-1])))
