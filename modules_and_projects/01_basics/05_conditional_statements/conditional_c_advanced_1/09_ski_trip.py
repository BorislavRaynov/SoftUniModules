days_stay = int(input())
type_room = input()
feedback = input()

nights_stay = days_stay - 1
total_price = 0

if type_room == "room for one person":
    total_price = nights_stay * 18
elif type_room == "apartment":
    total_price = nights_stay * 25
    if days_stay < 10:
        total_price = total_price * 0.70
    elif 10 <= days_stay <= 15:
        total_price = total_price * 0.65
    else:
        total_price = total_price * 0.50
elif type_room == "president apartment":
    total_price = nights_stay * 35
    if days_stay < 10:
        total_price = total_price * 0.90
    elif 10 <= days_stay <= 15:
        total_price = total_price * 0.85
    else:
        total_price = total_price * 0.80
if feedback == "positive":
    total_price = total_price * 1.25
else:
    total_price = total_price * 0.90
print(f"{total_price:.2f}")