def forecast(*args):

    locations = {"Sunny": [], "Cloudy": [], "Rainy": []}
    result = ""

    for el in args:
        city, weather = el[0], el[1]
        locations[weather].append(city)

    for item, value in locations.items():
        value.sort()
        for city in value:
            result += f"{city} - {item}" + "\n"

    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
