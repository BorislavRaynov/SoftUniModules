activation_key = input()
command = input()

while command != "Generate":
    command = command.split(">>>")
    current_command = command[0]

    if current_command == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif current_command == "Flip":
        needed_letters = command[1].split("/")
        start_index = int(command[2])
        end_index = int(command[3])
        manipulated_letters = activation_key[start_index:end_index:]
        if needed_letters[0] == "Upper":
            activation_key = activation_key.replace(manipulated_letters, manipulated_letters.upper())
        elif needed_letters[0] == "Lower":
            activation_key = activation_key.replace(manipulated_letters, manipulated_letters.lower())
        print(activation_key)

    elif current_command == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key[:start_index:] + activation_key[end_index::]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
