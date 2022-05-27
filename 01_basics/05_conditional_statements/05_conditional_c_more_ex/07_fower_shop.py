import math
count_magn = int(input())
count_zumb = int(input())
count_rose = int(input())
count_cactus = int(input())
gift_price = float(input())

price_magn = count_magn * 3.25
price_zumb = count_zumb * 4
price_rose = count_rose * 3.5
price_cactus = count_cactus * 8
total_price = price_magn + price_zumb + price_rose + price_cactus
final_price = total_price * 0.95

diff = abs(gift_price - final_price)

if final_price < gift_price:
    print(f"She will have to borrow {math.ceil(diff)} leva.")
else:
    print(f"She is left with {math.floor(diff)} leva.")
