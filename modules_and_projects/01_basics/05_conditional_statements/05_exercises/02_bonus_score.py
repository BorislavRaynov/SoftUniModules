num = int(input())

if num <= 100:
    num_b = num + 5
    b = num_b - num
elif num <= 1000:
    num_b = num * 1.2
    b = num_b - num
else:
    num_b = num * 1.1
    b = num_b - num

if num % 2 == 0:
    num_b = num_b + 1
    b = num_b - num
if num % 10 == 5:
    num_b = num_b + 2
    b = num_b - num
print(b)
print(num_b)