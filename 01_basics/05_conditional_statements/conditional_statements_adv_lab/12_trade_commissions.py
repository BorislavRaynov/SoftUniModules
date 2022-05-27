city = input()
sales = float(input())
city_is_valid = True
sales_is_valid = True
commision = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        commision = 0.05
    elif 500 < sales <= 1000:
        commision = 0.07
    elif 1000 < sales <= 10000:
        commision = 0.08
    elif sales > 10000:
        commision = 0.12
    else:
        sales_is_valid = False
elif city == "Varna":
    if 0 <= sales <= 500:
        commision = 0.045
    elif 500 < sales <= 1000:
        commision = 0.075
    elif 1000 <sales <= 10000:
        commision = 0.10
    elif sales > 10000:
        commision = 0.13
    else:
        sales_is_valid = False
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commision = 0.055
    elif 500 < sales <= 1000:
        commision = 0.08
    elif 100 < sales <= 10000:
        commision = 0.12
    elif sales > 10000:
        commision = 0.145
    else:
        sales_is_valid = False
else:
    city_is_valid = False
if city_is_valid and sales_is_valid:
    result = sales * commision
    print(f"{result:.2f}")
else:
    print("error")