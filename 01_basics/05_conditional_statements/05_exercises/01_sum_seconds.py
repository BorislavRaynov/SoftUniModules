racer_one = int(input())
racer_two = int(input())
racer_three = int(input())

total_sec_all = racer_one + racer_two + racer_three
total_min = total_sec_all // 60
total_sec = total_sec_all % 60
if total_sec <= 9:
    print(f'{total_min}:0{total_sec}')
else:
    print(f'{total_min}:{total_sec}')