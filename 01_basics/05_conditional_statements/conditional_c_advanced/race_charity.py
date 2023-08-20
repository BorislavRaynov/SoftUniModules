count_juniors = int(input())
count_seniors = int(input())
type_roads = input()

if type_roads == "trail":
    tax = count_juniors * 5.50 + count_seniors * 7
    charity_amount = tax * 0.95
elif type_roads == "downhill":
    tax = count_juniors * 12.25 + count_seniors * 13.75
    charity_amount = tax * 0.95
elif type_roads == "road":
    tax = count_juniors * 20 + count_seniors * 21.50
    charity_amount = tax * 0.95
elif type_roads == "cross-country":
    if count_juniors + count_seniors >= 50:
        tax = (count_juniors * 8 + count_seniors * 9.5) * 0.75
        charity_amount = tax * 0.95
    else:
        tax = count_juniors * 8 + count_seniors * 9.5
        charity_amount = tax * 0.95
print(f"{charity_amount:.2f}")