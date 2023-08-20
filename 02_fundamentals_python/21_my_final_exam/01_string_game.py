text = input()
command = input()

while command != "Done":
    current_command = command.split()
    to_do = current_command[0]

    if to_do == "Change":
        char = current_command[1]
        replacement = current_command[2]
        text = text.replace(char, replacement)
        print(text)

    elif to_do == "Includes":
        substring = current_command[1]
        if substring in text:
            print(True)
        else:
            print(False)

    elif to_do == "End":
        current_substring = current_command[1]
        if text.endswith(current_substring):
            print(True)
        else:
            print(False)

    elif to_do == "Uppercase":
        text = text.upper()
        print(text)

    elif to_do == "FindIndex":
        current_char = current_command[1]
        print(text.index(current_char))

    elif to_do == "Cut":
        start_index = int(current_command[1])
        count = int(current_command[2])
        text = text[start_index: start_index + count:]
        print(text)

    command = input()
