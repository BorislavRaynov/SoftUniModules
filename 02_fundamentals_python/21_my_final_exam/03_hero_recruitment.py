command = input()

my_heroes = {}

while command != "End":
    current_command = command.split()
    to_do = current_command[0]
    hero_name = current_command[1]

    if to_do == "Enroll":
        if hero_name not in my_heroes:
            my_heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif to_do == "Learn":
        spell_name = current_command[2]
        if hero_name not in my_heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in my_heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            my_heroes[hero_name].append(spell_name)

    elif to_do == "Unlearn":
        current_spell_name = current_command[2]
        if hero_name not in my_heroes:
            print(f"{hero_name} doesn't exist.")
        elif current_spell_name not in my_heroes[hero_name]:
            print(f"{hero_name} doesn't know {current_spell_name}.")
        else:
            my_heroes[hero_name].remove(current_spell_name)

    command = input()

print("Heroes:")
for hero, spell in my_heroes.items():
    print(f"== {hero}: {', '.join(spell)}")
