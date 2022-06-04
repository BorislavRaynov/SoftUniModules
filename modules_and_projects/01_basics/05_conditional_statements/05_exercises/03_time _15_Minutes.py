hours = int(input())
mins = int(input())

total_mins = hours * 60 + mins + 15

total_h = total_mins // 60
total_m = total_mins % 60

if total_h > 23:
    total_h = 0
if total_m < 10:
    print(f'{total_h}:0{total_m}')
else:
    print(f'{total_h}:{total_m}')