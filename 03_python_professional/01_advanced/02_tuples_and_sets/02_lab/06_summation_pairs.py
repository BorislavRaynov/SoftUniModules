nums = list(map(int, input().split()))
target_num = int(input())

for num in nums:
    sec_nums = nums
    sec_nums.remove(num)
    for n in sec_nums:
        if num + n == target_num:
            print(f"{num} + {n} = {target_num}")
            sec_nums.remove(n)
