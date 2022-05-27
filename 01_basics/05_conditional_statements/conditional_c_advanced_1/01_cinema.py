type_of_projection = input()
count_r = int(input())
count_c = int(input())

price = 0
if type_of_projection == "Premiere":
    price = count_r * count_c * 12
elif type_of_projection == "Normal":
    price = count_r * count_c * 7.50
else:
    price = count_r * count_c * 5
print(f"{price:.2f} leva")