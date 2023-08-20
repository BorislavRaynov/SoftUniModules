status_pirate_ship = list(map(int, input().split(">")))
status_war_ship = list(map(int, input().split(">")))
max_ship_section_health = int(input())
command = input().split()

section_in_war_ship_is_broken = False
section_in_pirate_ship_is_broken = False

while command[0] != "Retire":
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(status_war_ship):
            status_war_ship[index] -= damage
            if status_war_ship[index] <= 0:
                section_in_war_ship_is_broken = True
                break
        else:
            command = input().split()
            continue
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        current_damage = int(command[3])
        if 0 <= start_index < len(status_pirate_ship) and 0 <= end_index < len(status_pirate_ship):
            for section in range(start_index, end_index + 1):
                status_pirate_ship[section] -= current_damage
                if status_pirate_ship[section] <= 0:
                    section_in_pirate_ship_is_broken = True
                    break
        else:
            command = input().split()
            continue
    elif command[0] == "Repair":
        current_index = int(command[1])
        health = int(command[2])
        if 0 <= current_index < len(status_pirate_ship):
            status_pirate_ship[current_index] += health
            if status_pirate_ship[current_index] > max_ship_section_health:
                status_pirate_ship[current_index] = max_ship_section_health
        else:
            command = input().split()
            continue
    elif command[0] == "Status":
        count_sections_to_be_repaired = 0
        for section in status_pirate_ship:
            if section < max_ship_section_health * 0.2:
                count_sections_to_be_repaired += 1
        print(f"{count_sections_to_be_repaired} sections need repair.")

    if section_in_war_ship_is_broken or section_in_pirate_ship_is_broken:
        break
    command = input().split()

if not section_in_pirate_ship_is_broken and not section_in_war_ship_is_broken:
    print(f"Pirate ship status: {sum(status_pirate_ship)}")
    print(f"Warship status: {sum(status_war_ship)}")
if section_in_war_ship_is_broken:
    print("You won! The enemy ship has sunken.")
elif section_in_pirate_ship_is_broken:
    print("You lost! The pirate ship has sunken.")
