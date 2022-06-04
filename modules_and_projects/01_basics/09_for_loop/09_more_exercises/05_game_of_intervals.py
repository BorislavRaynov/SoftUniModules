num_moves = int(input())

init_result = 0
count_to_9 = 0
count_to_19 = 0
count_to_29 = 0
count_to_39 = 0
count_to_50 = 0
count_invalid = 0

for i in range(1, num_moves + 1):
    num = int(input())
    if num < 0 or num > 50:
        count_invalid += 1
        init_result /= 2
    elif 0 <= num <= 9:
        count_to_9 += 1
        init_result += num * 0.2
    elif num <= 19:
        count_to_19 += 1
        init_result += num * 0.3
    elif num <= 29:
        count_to_29 += 1
        init_result += num * 0.4
    elif num <= 39:
        count_to_39 += 1
        init_result += 50
    elif num <= 50:
        count_to_50 += 1
        init_result += 100

total_count = count_invalid + count_to_9 + count_to_19 + count_to_29 + count_to_39 + count_to_50
print(f"{init_result:.2f}")
print(f"From 0 to 9: {(count_to_9 / total_count) * 100:.2f}%")
print(f"From 10 to 19: {(count_to_19 / total_count) * 100:.2f}%")
print(f"From 20 to 29: {(count_to_29 / total_count) * 100:.2f}%")
print(f"From 30 to 39: {(count_to_39 / total_count) * 100:.2f}%")
print(f"From 40 to 50: {(count_to_50 / total_count) * 100:.2f}%")
print(f"Invalid numbers: {(count_invalid / total_count) * 100:.2f}%")