list_of_nums = list(map(int, input().split(", ")))

current_group = 10
lst = []

while len(list_of_nums) != 0:
    lst = [num for num in list_of_nums if num <= current_group]
    for num in lst:
        list_of_nums.remove(num)
    print(f"Group of {current_group}'s: {lst}")
    current_group += 10
    lst = []
