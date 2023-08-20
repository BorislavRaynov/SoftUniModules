info = input().split()
main_items = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item_obtained = False

while not legendary_item_obtained:
    for element in range(0, len(info), 2):
        key = info[element + 1].lower()
        value = int(info[element])
        if key not in main_items:
            main_items[key] = 0
        main_items[key] += value
        if main_items[key] >= 250:
            if key == "shards":
                print(f"Shadowmourne obtained!")
                legendary_item_obtained = True
                main_items[key] -= 250
                break
            elif key == "fragments":
                print(f"Valanyr obtained!")
                legendary_item_obtained = True
                main_items[key] -= 250
                break
            elif key == "motes":
                print(f"Dragonwrath obtained!")
                legendary_item_obtained = True
                main_items[key] -= 250
                break

    if legendary_item_obtained:
        break

    info = input().split()

for key, value in main_items.items():
    print(f"{key}: {value}")
