neighborhood = list(map(int, input().split("@")))
command = input()
mission_was_successful = False
current_index = 0

while command != "Love!":

    command_split = command.split()
    step = int(command_split[1])

    if current_index + step <= len(neighborhood) - 1:
        current_index += step
        if neighborhood[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighborhood[current_index] -= 2
            if neighborhood[current_index] == 0:
                print(f"Place {current_index} has Valentine's day.")

    else:
        current_index = 0
        if neighborhood[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighborhood[current_index] -= 2
            if neighborhood[current_index] == 0:
                print(f"Place {current_index} has Valentine's day.")

    if neighborhood.count(0) == len(neighborhood):
        mission_was_successful = True

    command = input()

print(f"Cupid's last position was {current_index}.")
if mission_was_successful:
    print("Mission was successful.")
else:
    failed_houses = [house for house in neighborhood if house != 0]
    print(f"Cupid has failed {len(failed_houses)} places.")
