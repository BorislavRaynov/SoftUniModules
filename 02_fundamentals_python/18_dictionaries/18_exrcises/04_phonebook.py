info = input()
phonebook = {}
while "-" in info:
    current_info = info.split("-")
    name, number = current_info
    phonebook[name] = number

    info = input()

for contact in range(int(info)):
    searched_contact = input()
    if searched_contact in phonebook:
        print(f"{searched_contact} -> {phonebook[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")
