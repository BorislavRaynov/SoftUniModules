from collections import deque
starting_liters = int(input())
current_name = input()
people = deque()

while current_name != "Start":
    people.append(current_name)
    current_name = input()

command = input()

while command != "End":
    current_command = command.split()

    if "refill" in current_command:
        starting_liters += int(current_command[1])

    else:
        current_liters = int(current_command[0])

        if starting_liters >= current_liters:
            print(f"{people.popleft()} got water")
            starting_liters -= current_liters

        else:
            print(f"{people.popleft()} must wait")

    command = input()

print(f"{starting_liters} liters left")
