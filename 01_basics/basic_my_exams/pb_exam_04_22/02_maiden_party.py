party_price = float(input())
count_love_wishes = int(input())
count_roses = int(input())
count_key_holders = int(input())
count_paintings = int(input())
count_lucky_surprise = int(input())

price_love_wishes = 0.60
price_roses = 7.20
price_key_holders = 3.60
price_paintings = 18.20
price_lucky_surprise = 22

total_love_wishes = count_love_wishes * price_love_wishes
total_roses = count_roses * price_roses
total_key_holders = count_key_holders * price_key_holders
total_paintings = count_paintings * price_paintings
total_lucky_surprise = count_lucky_surprise * price_lucky_surprise

total_income = total_love_wishes + total_roses + total_key_holders + total_paintings + total_lucky_surprise
total_count = count_love_wishes + count_roses + count_key_holders + count_paintings + count_lucky_surprise

if total_count >= 25:
    total_income = total_income * 0.65

final_income = total_income * 0.90
diff = abs(final_income - party_price)

if final_income >= party_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
