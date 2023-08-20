from collections import deque

elf_energy = deque(map(int, input().split()))
materials = deque(map(int, input().split()))

total_energy = 0
toys_made = 0
cookie = 1
double_chocolate = 2

i = 0

while elf_energy and materials:
    i += 1
    current_elf = elf_energy.popleft()
    current_material = materials[-1]
    to_be_rewarded = False

    if current_elf < 5:
        continue

    if i % 15 == 0:
        if current_elf >= current_material * 2:
            total_energy += current_material * 2
            current_elf -= current_material * 2
            elf_energy.append(current_elf)
            materials.pop()
        else:
            to_be_rewarded = True

    elif i % 5 == 0:
        if current_elf >= current_material:
            total_energy += current_material
            current_elf -= current_material
            elf_energy.append(current_elf)
            materials.pop()
        else:
            to_be_rewarded = True

    elif i % 3 == 0:
        if current_elf >= current_material * 2:
            total_energy += current_material * 2
            current_elf -= current_material * 2
            toys_made += 2
            elf_energy.append(current_elf + cookie)
            materials.pop()
        else:
            to_be_rewarded = True

    elif current_elf >= current_material:
        total_energy += current_material
        current_elf -= current_material
        toys_made += 1
        elf_energy.append(current_elf + cookie)
        materials.pop()
    else:
        to_be_rewarded = True

    if to_be_rewarded:
        elf_energy.append(current_elf * double_chocolate)


print(f"Toys: {toys_made}")
print(f"Energy: {total_energy}")
if elf_energy:
    print(f"Elves left: {', '.join(map(str, elf_energy))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")
