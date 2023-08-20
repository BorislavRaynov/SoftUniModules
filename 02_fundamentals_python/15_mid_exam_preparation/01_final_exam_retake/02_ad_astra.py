import re

data = input()
pattern = r'([#|\|])([A-Za-z\s]+)\1([0-9][0-9]\/[0-9][0-9]\/[0-9][0-9])\1([0-9]{1,5})\1'
result = re.findall(pattern, data)
calories_per_day = 2000
total_calories = 0

for match in result:
    if match:
        total_calories += int(match[3])

count_days = total_calories // calories_per_day

print(f"You have food to last you for: {count_days} days!")
for match in result:
    if match:
        print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
