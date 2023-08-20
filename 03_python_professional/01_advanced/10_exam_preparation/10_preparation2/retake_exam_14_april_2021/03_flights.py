def flights(*args):
    flight_dict = {}
    limit = args.index("Finish")
    for i in range(0, limit, 2):
        city = args[i]
        passengers = args[i + 1]
        if city not in flight_dict:
            flight_dict[city] = 0
        flight_dict[city] += passengers

    return flight_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
