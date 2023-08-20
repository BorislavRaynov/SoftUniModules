initial_lst = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command_split = command.split()
    current_command = command_split[0]
    if current_command == "Urgent":
        item = command_split[1]
        if item not in initial_lst:
            initial_lst.insert(0, item)
    elif current_command == "Unnecessary":
        item_to_remove = command_split[1]
        if item_to_remove in initial_lst:
            initial_lst.remove(item_to_remove)
    elif current_command == "Correct":
        old_item = command_split[1]
        new_item = command_split[2]
        if old_item in initial_lst:
            current_index = initial_lst.index(old_item)
            initial_lst.remove(old_item)
            initial_lst.insert(current_index, new_item)
    elif current_command == "Rearrange":
        item_to_move = command_split[1]
        if item_to_move in initial_lst:
            index = initial_lst.index(item_to_move)
            initial_lst.append(initial_lst.pop(index))

print(", ".join(initial_lst))
