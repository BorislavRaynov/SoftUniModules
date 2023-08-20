season = input()
km_per_month = float(input())
price = 0

if km_per_month <= 5000:
    if season == "Spring":
        price = (km_per_month * 0.75 * 4) * 0.90
    elif season == "Autumn":
        price = (km_per_month * 0.75 * 4) * 0.90
    elif season == "Summer":
        price = (km_per_month * 0.90 * 4) * 0.90
    elif season == "Winter":
        price = (km_per_month * 1.05 * 4) * 0.90
elif km_per_month <= 10000:
    if season == "Spring":
        price = (km_per_month * 0.95 * 4) * 0.90
    elif season == "Autumn":
        price = (km_per_month * 0.95 * 4) * 0.90
    elif season == "Summer":
        price = (km_per_month * 1.10 * 4) * 0.90
    elif season == "Winter":
        price = (km_per_month * 1.25 * 4) * 0.90
elif km_per_month <= 20000:
    price = (km_per_month * 1.45 * 4) * 0.90

print(f"{price:.2f}")