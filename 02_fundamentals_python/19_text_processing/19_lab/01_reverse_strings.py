command = input()

while command != "end":
    new_command = command[::-1]
    print(f"{command} = {new_command}")
    command = input()
