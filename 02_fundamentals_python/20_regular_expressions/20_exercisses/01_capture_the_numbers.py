import re

data = input()
pattern = r'\d+'
result = []
while data:
    result += re.findall(pattern, data)

    data = input()

print(" ".join(result))
