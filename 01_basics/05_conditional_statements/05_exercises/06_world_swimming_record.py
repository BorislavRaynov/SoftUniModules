from math import floor
record = float(input())
distance_m = float(input())
sec_per_m = float(input())

m_distance = distance_m * sec_per_m
slowing_count = floor(distance_m / 15)
total_time = m_distance + slowing_count * 12.5
diff = abs(total_time - record)
if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')