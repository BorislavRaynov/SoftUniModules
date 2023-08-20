import re

data = input()
pattern = r'\=([A-Z][A-Za-z]{2,})\=|\/([A-Z][A-Za-z]{2,})\/'
cities = []
result = re.finditer(pattern, data)
for match in result:
    for city in match.groups():
        if city:
            cities.append(city)

travel_points = 0
for city in cities:
    travel_points += len(city)

print(f"Destinations: {', '.join(cities)}")
print(f"Travel Points: {travel_points}")
