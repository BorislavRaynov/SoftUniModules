trunk_capacity = float(input())
suitcase_capacity = input()

used_capacity = 0
count_suitcases = 0

while suitcase_capacity != "End":
    suitcase_capacity = float(suitcase_capacity)
    count_suitcases += 1
    if count_suitcases % 3 == 0:
        used_capacity += suitcase_capacity * 1.1
    else:
        used_capacity += suitcase_capacity
    if used_capacity > trunk_capacity:
        count_suitcases -= 1
        break
    suitcase_capacity = input()

if used_capacity > trunk_capacity:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {count_suitcases} suitcases loaded.")