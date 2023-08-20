count_names = int(input())
even_set = set()
odd_set = set()


def final_result(num, second_num):
    result_to_print = ""
    if sum(even_set) == sum(odd_set):
        result_to_print = odd_set.union(even_set)
    elif sum(odd_set) > sum(even_set):
        result_to_print = odd_set.difference(even_set)
    elif sum(odd_set) < sum(even_set):
        result_to_print = odd_set.symmetric_difference(even_set)
    return ", ".join(list(map(str, result_to_print)))


for name in range(1, count_names + 1):
    current_name = input()
    current_result = 0
    for char in current_name:
        current_result += ord(char)
    result = int(current_result / name)
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

print(final_result(sum(odd_set), sum(even_set)))
