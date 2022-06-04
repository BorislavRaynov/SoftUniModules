budget = float(input())
season = input()

type_of_rent = "0"
location = "0"
price = 0

if budget <= 1000:
    type_of_rent = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
elif 1000 <= budget <= 3000:
    type_of_rent = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60
else:
    type_of_rent = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.90

print(f"{location} - {type_of_rent} - {price:.2f}")
