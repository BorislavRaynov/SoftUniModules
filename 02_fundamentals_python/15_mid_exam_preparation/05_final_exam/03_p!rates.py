cities_info = input()
my_cities = {}

while cities_info != "Sail":
    cities_info = cities_info.split("||")
    city = cities_info[0]
    population = int(cities_info[1])
    gold = int(cities_info[2])
    if city not in my_cities:
        my_cities[city] = {}
        my_cities[city]["population"] = 0
        my_cities[city]["gold"] = 0
    my_cities[city]["population"] += population
    my_cities[city]["gold"] += gold

    cities_info = input()

command = input()

while command != "End":
    event = command.split("=>")
    to_do = event[0]
    town = event[1]

    if to_do == "Plunder":
        current_people = int(event[2])
        current_gold = int(event[3])
        my_cities[town]["population"] -= current_people
        my_cities[town]["gold"] -= current_gold
        print(f"{town} plundered! {current_gold} gold stolen, {current_people} citizens killed.")
        if my_cities[town]["population"] == 0 or my_cities[town]["gold"] == 0:
            print(f"{town} has been wiped off the map!")
            my_cities.pop(town)

    elif to_do == "Prosper":
        current_gold = int(event[2])
        if current_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            my_cities[town]["gold"] += current_gold
            total_gold = my_cities[town]["gold"]
            print(f"{current_gold} gold added to the city treasury. {town} now has {total_gold} gold.")

    command = input()

if len(my_cities) > 0:
    print(f"Ahoy, Captain! There are {len(my_cities)} wealthy settlements to go to:")
    for city, actives in my_cities.items():
        print(f"{city} -> Population: {actives['population']} citizens, Gold: {actives['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
