budget = float(input())
season = input()

type_of_class = "0"
type_of_car = "0"

if season == "Winter":
    type_of_car = "Jeep"
    if budget <= 100:
        type_of_class = "Economy class"
        price = budget * 0.65
    elif 100 < budget <= 500:
        type_of_class = "Compact class"
        price = budget * 0.80
    elif budget > 500:
        type_of_class = "Luxury class"
        price = budget * 0.90
elif season == "Summer":
    type_of_car = "Cabrio"
    if budget <= 100:
        type_of_class = "Economy class"
        price = budget * 0.35
    elif 100 < budget <= 500:
        type_of_class = "Compact class"
        price = budget * 0.45
    elif budget > 500:
        type_of_class = "Luxury class"
        type_of_car = "Jeep"
        price = budget * 0.90
print(type_of_class)
print(f"{type_of_car} - {price:.2f}")