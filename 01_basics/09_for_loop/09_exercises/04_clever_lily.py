age = int(input())
price_washing_machine = float(input())
toy_price = float(input())

count_toys = 0
init_sum = 0
sum_all = 0
brother_money = 0
for position in range(1, age + 1):
    if position % 2 == 0:
        init_sum += 10
        sum_all = init_sum + sum_all
        brother_money += 1
    else:
        count_toys += 1

total_price_toys = count_toys * toy_price
total_money = sum_all - brother_money + total_price_toys
diff = abs(total_money - price_washing_machine)
if total_money >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")