number_of_cars = int(input())
my_cars = {}

for i in range(number_of_cars):
    data = input().split("|")
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    my_cars[car] = {}
    my_cars[car]["mileage"] = mileage
    my_cars[car]["fuel"] = fuel

command = input()

while command != "Stop":
    info = command.split(" : ")
    current_command = info[0]
    current_car = info[1]

    if current_command == "Drive":
        current_distance = int(info[2])
        current_fuel = int(info[3])
        if my_cars[current_car]["fuel"] < current_fuel:
            print("Not enough fuel to make that ride")
        else:
            my_cars[current_car]["mileage"] += current_distance
            my_cars[current_car]["fuel"] -= current_fuel
            print(f"{current_car} driven for {current_distance} kilometers. {current_fuel} liters of fuel consumed.")
            if my_cars[current_car]["mileage"] >= 100000:
                print(f"Time to sell the {current_car}!")
                my_cars.pop(current_car)

    elif current_command == "Refuel":
        current_fuel = int(info[2])
        capacity = 75
        result = my_cars[current_car]["fuel"] + current_fuel
        my_cars[current_car]["fuel"] += current_fuel
        if my_cars[current_car]["fuel"] > capacity:
            my_cars[current_car]["fuel"] = capacity
            print(f"{current_car} refueled with {current_fuel - (result - capacity)} liters")
        else:
            print(f"{current_car} refueled with {current_fuel} liters")

    elif current_command == "Revert":
        current_mileage = int(info[2])
        my_cars[current_car]["mileage"] -= current_mileage
        print(f"{current_car} mileage decreased by {current_mileage} kilometers")
        if my_cars[current_car]["mileage"] < 10000:
            my_cars[current_car]["mileage"] = 10000

    command = input()
for car in my_cars:
    print(f"{car} -> Mileage: {my_cars[car]['mileage']} kms, Fuel in the tank: {my_cars[car]['fuel']} lt.")
