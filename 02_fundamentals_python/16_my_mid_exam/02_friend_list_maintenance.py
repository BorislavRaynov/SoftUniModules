lst_friends = input().split(", ")
command = input()

while command != "Report":
    command_split = command.split()
    current_command = command_split[0]

    if current_command == "Blacklist":
        name = command_split[1]
        if name in lst_friends:
            name_index = lst_friends.index(name)
            lst_friends.pop(name_index)
            lst_friends.insert(name_index, "Blacklisted")
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
            command = input()
            continue

    elif current_command == "Error":
        current_index = int(command_split[1])
        if 0 <= current_index <= len(lst_friends) - 1:
            if lst_friends[current_index] != "Blacklisted" and lst_friends[current_index] != "Lost":
                name_current = lst_friends.pop(current_index)
                lst_friends.insert(current_index, "Lost")
                print(f"{name_current} was lost due to an error.")

    elif current_command == "Change":
        index = int(command_split[1])
        new_name = command_split[2]
        if 0 <= index <= len(lst_friends) - 1:
            current_name = lst_friends.pop(index)
            lst_friends.insert(index, new_name)
            print(f"{current_name} changed his username to {new_name}.")

    command = input()

black_listed_friends = [name for name in lst_friends if name == "Blacklisted"]
lost_names = [name for name in lst_friends if name == "Lost"]

print(f"Blacklisted names: {len(black_listed_friends)}")
print(f"Lost names: {len(lost_names)}")
print(" ".join(lst_friends))
