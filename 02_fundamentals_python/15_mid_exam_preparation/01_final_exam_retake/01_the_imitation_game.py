text = input()
command = input()

while command != "Decode":
    current_command = command.split("|")
    to_do = current_command[0]

    if to_do == "Move":
        number_of_letters = int(current_command[1])
        text = text[number_of_letters::] + text[:number_of_letters:]

    elif to_do == "Insert":
        current_index = int(current_command[1])
        current_value = current_command[2]
        text = text[:current_index] + current_value + text[current_index::]

    elif to_do == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        text = text.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {text}")
