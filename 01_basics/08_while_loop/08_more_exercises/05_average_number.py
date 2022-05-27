count_n = int(input())

sum_numbers = 0

for num in range(1, count_n + 1):
    number = int(input())

    sum_numbers += number

average_sum = sum_numbers / count_n
print(f"{average_sum:.2f}")