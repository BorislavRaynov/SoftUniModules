lst_rooms = input()
splited_lst_rooms = lst_rooms.replace(" ", "|").split("|")
initial_health = 100
current_health = 100
initial_bitcoin = 0
count_room = 0
managed_to_go_through = True
for i in range(len(splited_lst_rooms)):
    command = ""
    number = 0
    if i % 2 == 0:
        command = splited_lst_rooms[i]
        number = int(splited_lst_rooms[i + 1])
        count_room += 1
    elif i % 2 != 0:
        continue
    if command == "potion":
        if current_health > initial_health - number:
            diff = initial_health - current_health
        else:
            diff = number
        print(f"You healed for {diff} hp.")
        current_health += number
        if current_health > initial_health:
            current_health = initial_health
        print(f"Current health: {current_health} hp.")
    elif command == "chest":
        initial_bitcoin += number
        print(f"You found {number} bitcoins.")
    else:
        attack_monster = number
        current_health -= attack_monster
        if current_health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {count_room}")
            managed_to_go_through = False
            exit()
        else:
            print(f"You slayed {command}.")
if managed_to_go_through:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoin}")
    print(f"Health: {current_health}")


