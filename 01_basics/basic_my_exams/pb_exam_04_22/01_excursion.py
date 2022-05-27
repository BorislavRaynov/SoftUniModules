count_group = int(input())
count_nights = int(input())
count_transport_cards = int(input())
count_museum_tickets = int(input())

price_per_night = 20
price_per_transport_card = 1.60
price_per_museum_ticket = 6

total_price_nights = count_group * count_nights * 20
total_price_transport = count_group * count_transport_cards * 1.6
total_price_museum = count_group * count_museum_tickets * 6

total_price = (total_price_nights + total_price_transport + total_price_museum) * 1.25

print(f"{total_price:.2f}")
