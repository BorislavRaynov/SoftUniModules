from collections import deque


def best_list_pureness(*args):
    list_of_nums = deque(args[0])
    number_k = args[1]
    result_dict = {}
    for i in range(number_k + 1):
        current_sum = 0
        for inx, value in enumerate(list_of_nums):
            current_sum += (inx * value)
        if current_sum not in result_dict:
            result_dict[current_sum] = []
        result_dict[current_sum].append(i)
        list_of_nums.appendleft(list_of_nums.pop())

    pureness_value = max(result_dict)
    count_rotations = min(result_dict[pureness_value])
    return f"Best pureness {pureness_value} after {count_rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
