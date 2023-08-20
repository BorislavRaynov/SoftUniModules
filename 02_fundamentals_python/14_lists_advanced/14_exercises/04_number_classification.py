all_num = list(map(int, input().split(", ")))

positive_nums = list(filter(lambda x: x >= 0, all_num))
negative_nums = [num for num in all_num if num < 0]
even_nums = [num for num in all_num if num % 2 == 0]
odd_nums = [num for num in all_num if num % 2 != 0]

print(f"Positive: {(', '.join(map(str, positive_nums)))}")
print(f"Negative: {(', '.join(map(str, negative_nums)))}")
print(f"Even: {(', '.join(map(str, even_nums)))}")
print(f"Odd: {(', '.join(map(str, odd_nums)))}")
