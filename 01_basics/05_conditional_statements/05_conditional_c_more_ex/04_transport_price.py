count_km = int(input())
type_of_travel = input()

if type_of_travel == "day":
    taxi_price = 0.70 + 0.79 * count_km
else:
    taxi_price = 0.70 + 0.90 * count_km

bus_price = 0.09 * count_km
train_price = 0.06 * count_km


if count_km < 20:
    print(f"{taxi_price:.2f}")

if 20 <= count_km < 100:
    print(f"{bus_price:.2f}")

if count_km >= 100:
    print(f"{train_price:.2f}")