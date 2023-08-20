from collections import deque
jobs = deque(map(int, input().split(', ')))

inx = int(input())
searched_job = jobs[inx]
total_cycles = 0
my_jobs = {}
for value, key in enumerate(jobs):
    my_jobs[value] = key

my_jobs_sorted = sorted(my_jobs.items(), key=lambda x: (x[1], x[0]))
for el in my_jobs_sorted:
    index = el[0]
    cycle = el[1]
    total_cycles += cycle
    if index == inx:
        break

print(total_cycles)
