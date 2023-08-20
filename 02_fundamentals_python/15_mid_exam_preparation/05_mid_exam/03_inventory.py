journal = input().split(", ")
some_commands = input()

while some_commands != "Craft!":
    lst_some_commands = some_commands.split(" - ")
    command = lst_some_commands[0]
    item = lst_some_commands[1]
    if command == "Collect":
        if item not in journal:
            journal.append(item)
    elif command == "Drop":
        if item in journal:
            journal.remove(item)
    elif command == "Renew":
        if item in journal:
            journal.append(item)
            journal.remove(item)
    elif command == "Combine Items":
        current_items = item.split(":")
        old_item = current_items[0]
        new_item = current_items[1]
        if old_item in journal:
            index = journal.index(old_item)
            journal.insert(index + 1, new_item)

    some_commands = input()

print(", ".join(journal))
