count_floors = int(input())
count_rooms = int(input())

letter = ""
for floor in range(count_floors, 0, -1):
    for room in range(0, count_rooms):
        if floor == count_floors:
            letter = "L"
        elif floor % 2 == 0 and floor != count_floors:
            letter = "O"
        else:
            letter = f"A"
        print(f"{letter}{floor}{room}", end=" ")
    print()

