budget = int(input())
season = input()
count_fisherman = int(input())

boat_price = 0

if season == "Spring":
    boat_price = 3000
    if count_fisherman <= 6:
        boat_price = boat_price * 0.90
    elif 7 <= count_fisherman <= 11:
        boat_price = boat_price * 0.85
    elif count_fisherman >= 12:
        boat_price = boat_price * 0.75
elif season == "Winter":
    boat_price = 2600
    if count_fisherman <= 6:
        boat_price = boat_price * 0.90
    elif 7 <= count_fisherman <= 11:
        boat_price = boat_price * 0.85
    elif count_fisherman >= 12:
        boat_price = boat_price * 0.75
else:
    boat_price = 4200
    if count_fisherman <= 6:
        boat_price = boat_price * 0.90
    elif 7 <= count_fisherman <= 11:
        boat_price = boat_price * 0.85
    elif count_fisherman >= 12:
        boat_price = boat_price * 0.75

if count_fisherman % 2 == 0:
    if season == "Autumn":
        boat_price = boat_price
    else:
        boat_price = boat_price * 0.95
else:
    boat_price = boat_price

diff = abs(budget - boat_price)

if budget >= boat_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")