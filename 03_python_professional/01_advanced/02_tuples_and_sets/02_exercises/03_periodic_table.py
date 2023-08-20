count_chemicals = int(input())
uniques = set()
for chem in range(count_chemicals):
    chem_info = input().split()
    for info in chem_info:
        uniques.add(info)
for element in uniques:
    print(element)
