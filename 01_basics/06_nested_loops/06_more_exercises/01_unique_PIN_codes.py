first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

for first_n in range(1, first_limit + 1):
    if first_n % 2 == 0:
        num1 = first_n
        for second_n in range(2, second_limit + 1):
            count_dels = 0
            for dels in range(1, second_n + 1):
                if second_n % dels == 0:
                    count_dels += 1
            if count_dels == 2:
                num2 = second_n
                for third_n in range(1, third_limit + 1):
                    if third_n % 2 == 0:
                        num3 = third_n
                        print(f"{num1} {num2} {num3}")