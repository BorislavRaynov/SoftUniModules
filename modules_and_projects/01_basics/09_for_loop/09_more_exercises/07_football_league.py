stadium_capacity = int(input())
count_fans_total = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(1,count_fans_total + 1):
    fan_sector = input()
    if fan_sector == "A":
        sector_a += 1
    elif fan_sector == "B":
        sector_b += 1
    elif fan_sector == "V":
        sector_v += 1
    elif fan_sector == "G":
        sector_g += 1

sector_a_percent = (sector_a / count_fans_total) * 100
sector_b_percent = (sector_b / count_fans_total) * 100
sector_v_percent = (sector_v / count_fans_total) * 100
sector_g_percent = (sector_g / count_fans_total) * 100
total_percent = (count_fans_total / stadium_capacity) * 100

print(f"{sector_a_percent:.2f}%")
print(f"{sector_b_percent:.2f}%")
print(f"{sector_v_percent:.2f}%")
print(f"{sector_g_percent:.2f}%")
print(f"{total_percent:.2f}%")