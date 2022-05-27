month_of_the_year = input()
count_nights = int(input())

price_studio = 0
price_apartment = 0

if month_of_the_year == "May" or month_of_the_year == "October":
    price_studio = count_nights * 50
    price_apartment = count_nights * 65
    if 7 < count_nights <= 14:
        price_studio = price_studio * 0.95
    elif count_nights > 14:
        price_studio = price_studio * 0.70
        price_apartment = price_apartment * 0.90
elif month_of_the_year == "June" or month_of_the_year == "September":
    price_studio = count_nights * 75.20
    price_apartment = count_nights * 68.70
    if count_nights > 14:
        price_studio = price_studio * 0.80
        price_apartment = price_apartment * 0.90
elif month_of_the_year == "July" or month_of_the_year == "August":
    price_studio = count_nights * 76
    price_apartment = count_nights * 77
    if count_nights > 14:
        price_apartment = price_apartment * 0.90

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")