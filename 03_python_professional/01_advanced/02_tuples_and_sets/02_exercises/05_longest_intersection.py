count_inters = int(input())
all_results = {}
for i in range(count_inters):
    first_range, second_range = input().split("-")
    start_first, end_first = map(int, first_range.split(","))
    start_second, end_second = map(int, second_range.split(","))
    first_set = set(n for n in range(start_first, end_first + 1))
    second_set = set(n for n in range(start_second, end_second + 1))
    result = first_set.intersection(second_set)
    all_results[tuple(result)] = len(result)

biggest_value = 0
for v in all_results.values():
    if v > biggest_value:
        biggest_value = v

for result, info in all_results.items():
    if info == biggest_value:
        print(f"Longest intersection is {list(result)} with length {info}")
