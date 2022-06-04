import math
needed_h_project = int(input())
total_days = int(input())
count_workers_overtime = int(input())

h_working = total_days * 0.9 * 8
h_overtime = total_days * count_workers_overtime * 2
total_h_working = math.floor(h_working + h_overtime)

diff = abs(needed_h_project - total_h_working)

if total_h_working >= needed_h_project:
    print(f"Yes!{diff} hours left.")
else:
    print(f"Not enough time!{diff} hours needed.")
