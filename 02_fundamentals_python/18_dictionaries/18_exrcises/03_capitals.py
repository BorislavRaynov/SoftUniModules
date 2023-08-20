country = input().split(", ")
capital = input().split(", ")
searched_dict = dict(zip(country, capital))
# searched_dict = {country[i]: capital[i] for i in range(len(country))}

for country, capital in searched_dict.items():
    print(f"{country} -> {capital}")
