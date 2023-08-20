from collections import deque


doll = 150
wooden_train = 250
teddy_bear = 300
bicycle = 400

doll_is_crafted = False
w_train_is_crafted = False
t_bear_is_crafted = False
bicycle_is_crafted = False
task_finished = False
toys_crafted = {}

box_materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

while box_materials and magic_levels:
    current_material = box_materials.pop()
    current_magic = magic_levels.popleft()
    total_points = current_material * current_magic

    if total_points == doll:
        if "Doll" not in toys_crafted:
            toys_crafted["Doll"] = 0
        toys_crafted["Doll"] += 1
        doll_is_crafted = True
    elif total_points == wooden_train:
        if "Wooden train" not in toys_crafted:
            toys_crafted["Wooden train"] = 0
        toys_crafted["Wooden train"] += 1
        w_train_is_crafted = True
    elif total_points == teddy_bear:
        if "Teddy bear" not in toys_crafted:
            toys_crafted["Teddy bear"] = 0
        toys_crafted["Teddy bear"] += 1
        t_bear_is_crafted = True
    elif total_points == bicycle:
        if "Bicycle" not in toys_crafted:
            toys_crafted["Bicycle"] = 0
        toys_crafted["Bicycle"] += 1
        bicycle_is_crafted = True

    else:
        if total_points < 0:
            total_points = current_material + current_magic
            box_materials.append(total_points)
        elif total_points > 0:
            new_material = current_material + 15
            box_materials.append(new_material)
        else:
            if current_material != 0:
                box_materials.append(current_material)
            elif current_magic != 0:
                magic_levels.appendleft(current_magic)

if (doll_is_crafted and w_train_is_crafted) or (t_bear_is_crafted and bicycle_is_crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if box_materials:
    materials = reversed(box_materials)
    print(f"Materials left: {', '.join(str(magic) for magic in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(magic) for magic in magic_levels)}")
for name, count in sorted(toys_crafted.items()):
    print(f"{name}: {count}")
