count_dogr = int(input())
type_dogr = input()
type_dilivery = input()

total_price = 0

if count_dogr < 10:
    print("Invalid order")
else:
    if type_dogr == "90X130":
        if count_dogr < 30:
            total_price = count_dogr * 110
        elif count_dogr <= 60:
            total_price = count_dogr * 110 * 0.95
        else:
            total_price = count_dogr * 110 * 0.92

    elif type_dogr == "100X150":
        if count_dogr < 40:
            total_price = count_dogr * 140
        elif count_dogr <= 80:
            total_price = count_dogr * 140 * 0.94
        else:
            total_price = count_dogr * 140 * 0.90

    elif type_dogr == "130X180":
        if count_dogr < 20:
            total_price = count_dogr * 190
        elif count_dogr <= 50:
            total_price = count_dogr * 190 * 0.93
        else:
            total_price = count_dogr * 190 * 0.88

    elif type_dogr == "200X300":
        if count_dogr < 25:
            total_price = count_dogr * 250
        elif count_dogr <= 50:
            total_price = count_dogr * 250 * 0.91
        else:
            total_price = count_dogr * 250 * 0.86

    if type_dilivery == "With delivery":
        total_price += 60
    if count_dogr > 99:
        total_price = total_price * 0.96

    print(f"{total_price:.2f} BGN")
