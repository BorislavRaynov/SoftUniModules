message = input()
command = input()

while command != "Reveal":
    info = command.split(":|:")
    current_command = info[0]

    if current_command == "InsertSpace":
        given_index = int(info[1])
        message = message[:given_index:] + " " + message[given_index::]

    elif current_command == "Reverse":
        given_substring = info[1]
        if given_substring in message:
            new_string = given_substring[::-1]
            message = message.replace(given_substring, "", 1)
            message += new_string
        else:
            print("error")
            command = input()
            continue

    elif current_command == "ChangeAll":
        current_substring = info[1]
        replacement = info[2]
        while current_substring in message:
            message = message.replace(current_substring, replacement)

    print(message)
    command = input()

print(f"You have a new text message: {message}")
