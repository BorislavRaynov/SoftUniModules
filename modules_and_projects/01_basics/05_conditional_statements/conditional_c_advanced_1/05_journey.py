budget = float(input())
season = input()

location = ""
type_of_rent = ""

if season == "summer":
    type_of_rent = "Camp"
else:
    type_of_rent = "Hotel"

if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        price = budget * 0.30
    else:
        price = budget * 0.70
elif budget <= 1000:
    location = "Balkans"
    if season == "summer":
        price = budget * 0.40
    else:
        price = budget * 0.80
else:
    location = "Europe"
    type_of_rent = "Hotel"
    price = budget * 0.90

print(f"Somewhere in {location}")
print(f"{type_of_rent} - {price:.2f}")