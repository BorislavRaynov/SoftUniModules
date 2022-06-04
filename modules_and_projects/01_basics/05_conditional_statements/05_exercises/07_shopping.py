budget = float(input())
video_cards_count = int(input())
procs_count = int(input())
ram_count = int(input())

price_video_cards = video_cards_count * 250
price_procs = price_video_cards * 0.35 * procs_count
price_ram = price_video_cards * 0.1 * ram_count
total_price = price_video_cards + price_procs + price_ram

if video_cards_count > procs_count:
    total_price = total_price * 0.85

diff = abs(total_price - budget)

if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')