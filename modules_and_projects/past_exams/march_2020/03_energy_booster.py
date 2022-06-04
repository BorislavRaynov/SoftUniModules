fruit = input()
size_set = input()
count_sets = int(input())

total_price = 0

if fruit == "Watermelon":
    if size_set == "small":
        total_price = 2 * count_sets * 56
    elif size_set == "big":
        total_price = 5 * count_sets * 28.70
elif fruit == "Mango":
    if size_set == "small":
        total_price = 2 * count_sets * 36.66
    elif size_set == "big":
        total_price = 5 * count_sets * 19.60
elif fruit == "Pineapple":
    if size_set == "small":
        total_price = 2 * count_sets * 42.10
    elif size_set == "big":
        total_price = 5 * count_sets * 24.80
elif fruit == "Raspberry":
    if size_set == "small":
        total_price = 2 * count_sets * 20
    elif size_set == "big":
        total_price = 5 * count_sets * 15.20

if 400 <= total_price <= 1000:
    total_price = total_price * 0.85
elif total_price > 1000:
    total_price = total_price * 0.5

print(f"{total_price:.2f} lv.")
