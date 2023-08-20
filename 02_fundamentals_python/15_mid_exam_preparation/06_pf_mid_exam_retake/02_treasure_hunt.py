initial_treasure_chest = input().split("|")
command = input().split()

initial_treasure_chest_is_empty = False

while command[0] != "Yohoho!":
    if command[0] == "Loot":
        lst_loots = command[1::]
        for loot in lst_loots:
            if loot in initial_treasure_chest:
                continue
            else:
                initial_treasure_chest.insert(0, loot)
    elif command[0] == "Drop":
        index = int(command[1])
        if index == -1:
            command = input().split()
            continue
        if index <= len(initial_treasure_chest) - 1:
            loot_to_be_moved = initial_treasure_chest.pop(index)
            initial_treasure_chest.append(loot_to_be_moved)
    elif command[0] == "Steal":
        count = int(command[1])
        stolen_items = []
        if len(initial_treasure_chest) <= count:
            initial_treasure_chest_is_empty = True
            stolen_items = initial_treasure_chest
        else:
            for item in range(count):
                stolen_items.insert(0, initial_treasure_chest[-1])
                initial_treasure_chest.remove(initial_treasure_chest[-1])
        print(", ".join(stolen_items))
    command = input().split()

if initial_treasure_chest_is_empty:
    print("Failed treasure hunt.")
else:
    sum_all_items_len = 0
    for item in initial_treasure_chest:
        sum_all_items_len += len(item)
    average_gain = sum_all_items_len / len(initial_treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
