trip_price = float(input())
puzls_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_price = puzls_count * 2.6 + dolls_count * 3 + bears_count * 4.1 + minions_count * 8.2 + trucks_count * 2
total_count = puzls_count + dolls_count + bears_count + minions_count + trucks_count

if total_count >= 50:
    total_price = total_price * 0.75

final_price = total_price * 0.9
diff = abs(final_price - trip_price)
if final_price >= trip_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')