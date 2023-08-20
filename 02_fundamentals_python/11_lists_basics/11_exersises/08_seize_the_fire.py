given_level_of_fire = input().replace(" = ", "#").split("#")
amount_water = int(input())

effort = 0
used_water = 0
level_of_fire = 0

print("Cells:")

for type_of_fire in range(0, len(given_level_of_fire), 2):

    if given_level_of_fire[type_of_fire] == "High":
        current_index = type_of_fire
        level_of_fire = int(given_level_of_fire[current_index + 1])
        if 81 <= level_of_fire <= 125 and level_of_fire <= amount_water:
            cells.append(str(level_of_fire))
            used_water += level_of_fire
            amount_water -= level_of_fire
            effort += level_of_fire * 0.25
            print(f" - {level_of_fire}")

    elif given_level_of_fire[type_of_fire] == "Medium":
        current_index = type_of_fire
        level_of_fire = int(given_level_of_fire[current_index + 1])
        if 51 <= level_of_fire <= 80 and level_of_fire <= amount_water:
            cells.append(str(level_of_fire))
            used_water += level_of_fire
            amount_water -= level_of_fire
            effort += level_of_fire * 0.25
            print(f" - {level_of_fire}")

    elif given_level_of_fire[type_of_fire] == "Low":
        current_index = type_of_fire
        level_of_fire = int(given_level_of_fire[current_index + 1])
        if 1 <= level_of_fire <= 50 and level_of_fire <= amount_water:
            cells.append(str(level_of_fire))
            used_water += level_of_fire
            amount_water -= level_of_fire
            effort += level_of_fire * 0.25
            print(f" - {level_of_fire}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {used_water}")
