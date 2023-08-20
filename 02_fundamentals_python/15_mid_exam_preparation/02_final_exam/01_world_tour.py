text = input()
command = input()

while command != "Travel":
    current_command = command.split(":")
    to_do = current_command[0]

    if to_do == "Add Stop":
        current_index = int(current_command[1])
        current_string = current_command[2]

        if 0 <= current_index <= len(text) - 1:
            text = text[:current_index:] + current_string + text[current_index::]

    elif to_do == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if 0 <= start_index <= len(text) - 1 and 0 <= end_index <= len(text) - 1:
            text = text[:start_index:] + text[end_index + 1::]

    elif to_do == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        if old_string in text:
            text = text.replace(old_string, new_string)

    print(text)
    command = input()

print(f"Ready for world tour! Planned stops: {text}")
