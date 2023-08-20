password = input()

command = input()

while command != "Done":
    command = command.split()
    to_do = command[0]

    if to_do == "TakeOdd":
        password = password[1::2]

    elif to_do == "Cut":
        given_index = int(command[1])
        given_length = int(command[2])
        searched_string = password[given_index:given_index + given_length]
        password = password.replace(searched_string, "", 1)

    elif to_do == "Substitute":
        given_substring = command[1]
        given_substitute = command[2]
        if given_substring not in password:
            print("Nothing to replace!")
            command = input()
            continue
        else:
            password = password.replace(given_substring, given_substitute)

    print(password)
    command = input()

print(f"Your password is: {password}")
