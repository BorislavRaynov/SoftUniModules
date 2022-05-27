count_groups = int(input())

musala_people = 0
monblanc_people = 0
kilimanjaro_people = 0
k2_people = 0
everest_people = 0

for i in range(1, count_groups + 1):
    count_people = int(input())
    if count_people <= 5:
        musala_people += count_people
    elif count_people <= 12:
        monblanc_people += count_people
    elif count_people <= 25:
        kilimanjaro_people += count_people
    elif count_people <= 40:
        k2_people += count_people
    else:
        everest_people += count_people

total_people = musala_people + kilimanjaro_people + monblanc_people + k2_people + everest_people

musala_percent = (musala_people / total_people) * 100
monblanc_percent = (monblanc_people / total_people) * 100
kilimanjaro_percent = (kilimanjaro_people / total_people) * 100
k2_percent = (k2_people / total_people) * 100
everest_percent = (everest_people / total_people) * 100

print(f"{musala_percent:.2f}%")
print(f"{monblanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")