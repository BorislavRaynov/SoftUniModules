v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

litrs_p1 = p1 * h
litrs_p2 = p2 * h
total_litrs = litrs_p1 + litrs_p2

percent_p1 = (litrs_p1 / total_litrs) * 100
percent_p2 = (litrs_p2 / total_litrs) * 100
total_percent = ((litrs_p1 + litrs_p2) / v) * 100

diff = abs(total_litrs - v)

if v >= total_litrs:
    print(f"The pool is {total_percent}% full. Pipe 1: {percent_p1:.2f}%. Pipe 2: {percent_p2:.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {diff:.2f} liters.")