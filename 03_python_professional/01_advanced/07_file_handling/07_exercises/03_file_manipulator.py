import os

command = input()

while command != "End":
    command = command.split("-")
    current_command = command[0]
    file_name = command[1]

    if current_command == "Create":
        file = open(f'{file_name}', 'w')
        file.close()

    elif current_command == "Add":
        content = command[2]
        with open(f'{file_name}', 'a') as current_file:
            current_file.write(content + '\n')

    elif current_command == "Replace":
        old_string = command[2]
        new_string = command[3]
        try:
            with open(f'{file_name}', 'r') as current_file:
                lines = current_file.readlines()

            with open(f'{file_name}', 'w') as current_file:
                for i in range(len(lines)):
                    lines[i] = lines[i].replace(old_string, new_string)
                current_file.write("".join(lines))

        except FileNotFoundError:
            print("An error occurred")

    elif current_command == "Delete":
        try:
            os.remove(f'{file_name}')
        except FileNotFoundError:
            print("An error occurred")

    command = input()
