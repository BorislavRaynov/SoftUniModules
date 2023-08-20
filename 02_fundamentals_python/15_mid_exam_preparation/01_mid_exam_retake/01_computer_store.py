price = input()

total_price = 0

while price != "special" and price != "regular":
    current_price = float(price)
    if current_price < 0:
        print("Invalid price!")
    else:
        total_price += current_price

    price = input()

total_tax = total_price * 0.2
final_price = total_price + total_tax

if price == "special":
    final_price *= 0.9
if final_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {total_tax:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")
