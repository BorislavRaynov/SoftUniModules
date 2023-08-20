number_heroes = int(input())
max_hp = 100
max_mp = 200
my_heroes = {}

for heroes in range(number_heroes):
    data = input().split()
    name = data[0]
    hp = int(data[1])
    mp = int(data[2])
    my_heroes[name] = {}
    my_heroes[name]["HP"] = hp
    my_heroes[name]["MP"] = mp

command = input()

while command != "End":

    command = command.split(" - ")
    current_command = command[0]
    current_hero = command[1]

    if current_command == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if my_heroes[current_hero]["MP"] >= mp_needed:
            my_heroes[current_hero]["MP"] -= mp_needed
            current_mp = my_heroes[current_hero]["MP"]
            print(f"{current_hero} has successfully cast {spell_name} and now has {current_mp} MP!")
        else:
            print(f"{current_hero} does not have enough MP to cast {spell_name}!")

    elif current_command == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        my_heroes[current_hero]["HP"] -= damage
        if my_heroes[current_hero]["HP"] > 0:
            current_hp = my_heroes[current_hero]["HP"]
            print(f"{current_hero} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        else:
            my_heroes.pop(current_hero)
            print(f"{current_hero} has been killed by {attacker}!")

    elif current_command == "Recharge":
        amount = int(command[2])
        my_heroes[current_hero]["MP"] += amount
        if my_heroes[current_hero]["MP"] > max_mp:
            diff = amount - (my_heroes[current_hero]["MP"] - max_mp)
            print(f"{current_hero} recharged for {diff} MP!")
            my_heroes[current_hero]["MP"] = max_mp
        else:
            print(f"{current_hero} recharged for {amount} MP!")

    elif current_command == "Heal":
        current_amount = int(command[2])
        my_heroes[current_hero]["HP"] += current_amount
        if my_heroes[current_hero]["HP"] > max_hp:
            diff = current_amount - (my_heroes[current_hero]["HP"] - max_hp)
            my_heroes[current_hero]["HP"] = max_hp
            print(f"{current_hero} healed for {diff} HP!")
        else:
            print(f"{current_hero} healed for {current_amount} HP!")

    command = input()

for hero, data in my_heroes.items():
    print(hero)
    for hp, mp in data.items():
        print(f"  {hp}: {mp}")
