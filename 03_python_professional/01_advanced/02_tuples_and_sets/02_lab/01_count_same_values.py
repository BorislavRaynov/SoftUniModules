numbers = tuple(map(float, input().split()))
unique_nums = []
for num in numbers:
    if num not in unique_nums:
        unique_nums.append(num)
for n in unique_nums:
    print(f"{n} - {numbers.count(n)} times")
