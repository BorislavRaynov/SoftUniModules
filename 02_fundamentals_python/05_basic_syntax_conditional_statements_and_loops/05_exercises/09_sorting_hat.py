name = input()
place = ""
while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        place = "Gryffindor"
    elif len(name) == 5:
        place = "Slytherin"
    elif len(name) == 6:
        place = "Ravenclaw"
    elif len(name) > 6:
        place = "Hufflepuff"
    print(f"{name} goes to {place}.")
    name = input()

if name == "Welcome!":
    print(f"Welcome to Hogwarts.")
