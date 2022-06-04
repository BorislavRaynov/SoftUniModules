from math import floor
centuries = int(input())

cent_urie = 1 * centuries
years = 100 * cent_urie
days = 365.2422 * years
hours = 24 * floor(days)
minutes = 60 * hours

print(f"{cent_urie} centuries = {years} years = {floor(days)} days = {hours} hours = {minutes} minutes")
