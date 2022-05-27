count_mounts = int(input())

total_el_price = 0
total_water_price = 0
total_internet_price = 0
total_others_price = 0

for i in range(1, count_mounts + 1):
    el_price = float(input())
    total_el_price += el_price
    total_water_price += 20
    total_internet_price += 15
    total_others_price += (el_price + 15 + 20) * 1.2

average_price = (total_el_price + total_internet_price + total_others_price + total_water_price) / count_mounts
print(f"Electricity: {total_el_price:.2f} lv")
print(f"Water: {total_water_price:.2f} lv")
print(f"Internet: {total_internet_price:.2f} lv")
print(f"Other: {total_others_price:.2f} lv")
print(f"Average: {average_price:.2f} lv")