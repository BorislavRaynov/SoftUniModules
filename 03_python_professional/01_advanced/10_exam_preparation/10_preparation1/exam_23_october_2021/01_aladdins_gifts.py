from collections import deque


def material_made(amount, gift_limits):
    for key, value in gift_limits.items():
        if value[0] <= amount <= value[1]:
            return key
    return False


materials = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))

limits_of_gifts = {
    "Gemstone": [100, 199], "Porcelain Sculpture": [200, 299],
    "Gold": [300, 399], "Diamond Jewellery": [400, 499]
}

gifts_made = {
    "Diamond Jewellery": 0, "Gemstone": 0,
    "Gold": 0, "Porcelain Sculpture": 0
}

all_limits = [100, 499]

gemstone_crafted = False
sculpture_crafted = False
gold_crafted = False
jewellery_crafted = False

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    current_sum = current_material + current_magic

    if current_sum < 100:
        if current_sum % 2 == 0:
            current_material *= 2
            current_magic *= 3
            current_sum = current_magic + current_material
        else:
            current_material *= 2
            current_magic *= 2
            current_sum = current_magic + current_material

    elif current_sum > 499:
        current_sum /= 2

    elif all_limits[0] <= current_sum <= all_limits[1]:
        gift = material_made(current_sum, limits_of_gifts)

    gift = material_made(current_sum, limits_of_gifts)

    if gift:
        gifts_made[gift] += 1

for key, value in gifts_made.items():
    if value > 0:
        if key == 'Gemstone':
            gemstone_crafted = True
        elif key == 'Porcelain Sculpture':
            sculpture_crafted = True
        elif key == 'Gold':
            gold_crafted = True
        elif key == 'Diamond Jewellery':
            jewellery_crafted = True

if (gemstone_crafted and sculpture_crafted) or (gold_crafted and jewellery_crafted):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for key, value in gifts_made.items():
    if value:
        print(f"{key}: {value}")
