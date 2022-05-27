type_of_flower = input()
count_flowers = int(input())
budget = int(input())

price = 0
if type_of_flower == "Roses":
    if count_flowers > 80:
        price = (count_flowers * 5) * 0.90
    else:
        price = count_flowers * 5
elif type_of_flower == "Dahlias":
    if count_flowers > 90:
        price = (count_flowers * 3.80) * 0.85
    else:
        price = count_flowers * 3.80
elif type_of_flower == "Tulips":
    if count_flowers > 80:
        price = (count_flowers * 2.80) * 0.85
    else:
        price = count_flowers * 2.80
elif type_of_flower == "Narcissus":
    if count_flowers < 120:
        price = (count_flowers * 3) * 1.15
    else:
        price = count_flowers * 3
elif type_of_flower == "Gladiolus":
    if count_flowers < 80:
        price = (count_flowers * 2.50) * 1.20
    else:
        price = count_flowers * 2.50

diff = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {count_flowers} {type_of_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")