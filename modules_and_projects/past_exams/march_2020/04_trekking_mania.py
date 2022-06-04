count_groups = int(input())

total_musala = 0
total_monblanc = 0
total_kilimanjaro = 0
total_k2 = 0
total_everest = 0
total_people = 0

for group in range(1, count_groups + 1):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group <= 5:
        total_musala += people_in_group
    elif people_in_group <= 12:
        total_monblanc += people_in_group
    elif people_in_group <= 25:
        total_kilimanjaro += people_in_group
    elif people_in_group <= 40:
        total_k2 += people_in_group
    elif people_in_group > 40:
        total_everest += people_in_group

percent_musala = (total_musala / total_people) * 100
percent_monblanc = (total_monblanc / total_people) * 100
percent_kilimanjaro = (total_kilimanjaro / total_people) * 100
percent_k2 = (total_k2 / total_people) * 100
percent_everest = (total_everest / total_people) * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblanc:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
