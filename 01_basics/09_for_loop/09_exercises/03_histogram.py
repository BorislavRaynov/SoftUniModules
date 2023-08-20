count_numbers = int(input())

sum_p1 = 0
sum_p2 = 0
sum_p3 = 0
sum_p4 = 0
sum_p5 = 0

for num in range(1, count_numbers + 1):
    number = int(input())
    if number < 200:
        sum_p1 += 1
    elif number <= 399:
        sum_p2 += 1
    elif number <= 599:
        sum_p3 += 1
    elif number <= 799:
        sum_p4 += 1
    else:
        sum_p5 += 1

p1_percent = (sum_p1 / count_numbers) * 100
p2_percent = (sum_p2 / count_numbers) * 100
p3_percent = (sum_p3 / count_numbers) * 100
p4_percent = (sum_p4 / count_numbers) * 100
p5_percent = (sum_p5 / count_numbers) * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")