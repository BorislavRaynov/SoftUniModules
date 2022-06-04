start = int(input())
stop = int(input())
magic = int(input())

count_combinations = 0
current_combination = 0
combination_is_found = False
first_number = 0
second_number = 0

for first in range(start, stop + 1):
    for second in range(start, stop + 1):
        count_combinations += 1
        if first + second == magic:
            combination_is_found = True
            current_combination = count_combinations
            first_number = first
            second_number = second
            break
    if combination_is_found:
        break

if combination_is_found:
    print(f"Combination N:{count_combinations} ({first_number} + {second_number} = {magic})")
else:
    print(f"{count_combinations} combinations - neither equals {magic}")
