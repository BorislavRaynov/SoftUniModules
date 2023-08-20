num = int(input())

prime_num_is_found = False
count_dividers = 0
for divider in range(1, num + 1):
    if num % divider == 0:
        count_dividers += 1

if count_dividers == 2:
    prime_num_is_found = True

if prime_num_is_found:
    print(True)
else:
    print(False)
