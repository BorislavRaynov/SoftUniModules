count_numbers = int(input())
sum_left = 0
sum_right = 0
for number in range(2 * count_numbers):
    current_number = int(input())
    if number < count_numbers:
        sum_left += current_number
    else:
        sum_right += current_number
diff = abs(sum_left - sum_right)
if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {diff}")
