tax_per_year = int(input())

shoes = tax_per_year * 0.6
equip = shoes * 0.8
ball = equip / 4
acc = ball / 5

total = shoes + equip + ball + acc + tax_per_year
print(total)