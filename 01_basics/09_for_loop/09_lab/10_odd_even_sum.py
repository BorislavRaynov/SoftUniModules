count_num = int(input())
sum_even = 0
sum_odd = 0
for position in range(1, count_num + 1):
    current_number = int(input())
    if position % 2 == 0:
        sum_even += current_number
    else:
        sum_odd += current_number

diff = abs(sum_even - sum_odd)
if sum_even == sum_odd:
    print("Yes")
    print(f"Sum = {sum_even}")
else:
    print("No")
    print(f"Diff = {diff}")