import math
current_record_sec = float(input())
distance_m = float(input())
time_per_m_in_sec = float(input())

times_slowed = math.floor(distance_m / 50)
sec_slowed = times_slowed * 30
total_time = distance_m * time_per_m_in_sec
final_time = total_time + sec_slowed

if final_time < current_record_sec:
    print(f"Yes! The new record is {final_time:.2f} seconds.")
else:
    diff = abs(final_time - current_record_sec)
    print(f"No! He was {diff:.2f} seconds slower.")
