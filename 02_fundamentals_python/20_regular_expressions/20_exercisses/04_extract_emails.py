import re

data = input()
pattern = r'(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'

result = re.findall(pattern, data)

for match in result:
    print("".join(match[0]))
