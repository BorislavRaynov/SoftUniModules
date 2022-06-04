type_fuel = input()
liters_fuel = float(input())
card = input()

if type_fuel == "Gas":
    if card == "No":
        total_price = liters_fuel * 0.93
        if 20 <= liters_fuel <= 25:
            total_price = total_price * 0.92
            print(f"{total_price:.2f} lv.")
        elif liters_fuel > 25:
            total_price = total_price * 0.90
            print(f"{total_price:.2f} lv.")
        else:
            print(f"{total_price:.2f} lv.")
    if card == "Yes":
        total_price = liters_fuel * (0.93 - 0.08)
        if 20 <= liters_fuel <= 25:
            total_price = total_price * 0.92
            print(f"{total_price:.2f} lv.")
        elif liters_fuel > 25:
            total_price = total_price * 0.90
            print(f"{total_price:.2f} lv.")
        else:
            print(f"{total_price:.2f} lv.")
elif type_fuel == "Gasoline":
    if card == "No":
        total_price = liters_fuel * 2.22
        if 20 <= liters_fuel <= 25:
            total_price = total_price * 0.92
            print(f"{total_price:.2f} lv.")
        elif liters_fuel > 25:
            total_price = total_price * 0.90
            print(f"{total_price:.2f} lv.")
        else:
            print(f"{total_price:.2f} lv.")
    if card == "Yes":
        total_price = liters_fuel * (2.22 - 0.18)
        if 20 <= liters_fuel <= 25:
            total_price = total_price * 0.92
            print(f"{total_price:.2f} lv.")
        elif liters_fuel > 25:
            total_price = total_price * 0.90
            print(f"{total_price:.2f} lv.")
        else:
            print(f"{total_price:.2f} lv.")
elif type_fuel == "Diesel":
    if card == "No":
        total_price = liters_fuel * 2.33
        if 20 <= liters_fuel <= 25:
            total_price = total_price * 0.92
            print(f"{total_price:.2f} lv.")
        elif liters_fuel > 25:
            total_price = total_price * 0.90
            print(f"{total_price:.2f} lv.")
        else:
            print(f"{total_price:.2f} lv.")
    if card == "Yes":
        total_price = liters_fuel * (2.33 - 0.12)
        if 20 <= liters_fuel <= 25:
            total_price = total_price * 0.92
            print(f"{total_price:.2f} lv.")
        elif liters_fuel > 25:
            total_price = total_price * 0.90
            print(f"{total_price:.2f} lv.")
        else:
            print(f"{total_price:.2f} lv.")