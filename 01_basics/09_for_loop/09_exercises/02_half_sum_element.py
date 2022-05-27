import sys

count_num = int(input())
max_num = -sys.maxsize
sum = 0
for i in range(1, count_num + 1):
    num = int(input())
    if num > max_num:
        max_num = num
    sum += num
if max_num == sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs((sum - max_num) - max_num)
    print("No")
    print(f"Diff = {diff}")