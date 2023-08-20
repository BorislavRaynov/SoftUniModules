given_lst = list(map(int, input().split()))
average_sum = sum(given_lst) / len(given_lst)
all_above_average = sorted([num for num in given_lst if num > average_sum], reverse=True)

if len(all_above_average) == 0:
    print("No")
elif len(all_above_average) <= 5:
    print(" ".join(list(map(str, all_above_average))))
else:
    print(" ".join(list(map(str, all_above_average[:5:]))))
