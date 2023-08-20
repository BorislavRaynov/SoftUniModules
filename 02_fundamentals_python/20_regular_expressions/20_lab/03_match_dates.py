import re
data = input()
pattern = r'\b([0-9]{2})([,-\/])([A-Z]{1}[a-z]{2})\2([0-9]{4})'
match = re.findall(pattern, data)

for m in match:
    print(f"Day: {m[0]}, Month: {m[2]}, Year: {m[3]}")
