number = int(input())

first_end = number % 10
second_end = int((number / 10) % 10)
third_end = int((number / 100) % 10)

for first_multiplayer in range(1, first_end + 1):
    for second_multiplayer in range(1, second_end + 1):
        for third_multilayer in range(1, third_end + 1):
            result = first_multiplayer * second_multiplayer * third_multilayer
            print(f"{first_multiplayer} * {second_multiplayer} * {third_multilayer} = {result};")
