number_of_lines = int(input())
capacity = 255
total_ltrs = 0
for pours in range(number_of_lines):
    poured_ltrs = int(input())
    if capacity < poured_ltrs:
        print("Insufficient capacity!")
        continue
    capacity -= poured_ltrs
    total_ltrs += poured_ltrs
print(total_ltrs)
