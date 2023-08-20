length_set1, length_set2 = list(map(int, input().split()))
set1 = set()
set2 = set()
for element in range(1, length_set1 + length_set2 + 1):
    if element <= length_set1:
        set1.add(input())
    else:
        set2.add(input())

for el in set1.intersection(set2):
    print(el)
