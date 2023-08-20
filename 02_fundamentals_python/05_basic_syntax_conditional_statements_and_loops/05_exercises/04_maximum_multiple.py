divisor = int(input())
boundary = int(input())
asked_number = 0
for number in range(divisor, boundary + 1):
    if number % divisor == 0:
        asked_number = number

print(asked_number)
