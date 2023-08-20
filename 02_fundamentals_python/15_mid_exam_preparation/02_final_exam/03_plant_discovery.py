num = int(input())

discovered_plants = {}

for info in range(num):
    data = input().split("<->")
    plant = data[0]
    rarity = int(data[1])
    if plant not in discovered_plants:
        discovered_plants[plant] = {}
        discovered_plants[plant]["rarity"] = 0
    discovered_plants[plant]["rarity"] = rarity

command = input()

for plant in discovered_plants:
    discovered_plants[plant]["rating"] = []

while command != "Exhibition":
    current_command = command.split(": ")
    to_do = current_command[0]
    additional_info = current_command[1].split(" - ")
    plant = additional_info[0]
    if plant not in discovered_plants:
        print("error")
    else:
        if to_do == "Rate":
            rating = int(additional_info[1])
            discovered_plants[plant]["rating"].append(rating)
        elif to_do == "Update":
            new_rarity = int(additional_info[1])
            discovered_plants[plant]["rarity"] = new_rarity
        elif to_do == "Reset":
            discovered_plants[plant]["rating"].clear()

    command = input()
print("Plants for the exhibition:")
for plant, info in discovered_plants.items():
    if sum(discovered_plants[plant]["rating"]) == 0:
        average_rating = 0
    else:
        average_rating = sum(discovered_plants[plant]["rating"]) / len(discovered_plants[plant]["rating"])
    print(f"- {plant}; Rarity: {discovered_plants[plant]['rarity']}; Rating: {average_rating:.2f}")
