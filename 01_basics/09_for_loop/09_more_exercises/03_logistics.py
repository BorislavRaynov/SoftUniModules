count_loads = int(input())

van_tons = 0
truck_tons = 0
train_tons = 0

for i in range(1, count_loads + 1):
    tons_per_load = int(input())
    if tons_per_load <= 3:
        van_tons += tons_per_load
    elif tons_per_load <= 11:
        truck_tons += tons_per_load
    elif tons_per_load >= 12:
        train_tons += tons_per_load

total_tons = van_tons + truck_tons + train_tons
total_price = van_tons * 200 + truck_tons * 175 + train_tons * 120
average_price_per_ton = total_price / total_tons
van_percent = (van_tons / total_tons) * 100
truck_percent = (truck_tons / total_tons) * 100
train_percent = (train_tons / total_tons) * 100

print(f"{average_price_per_ton:.2f}")
print(f"{van_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")