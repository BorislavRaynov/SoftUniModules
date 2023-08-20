import re

data = input()
pattern = r'(w{3}\.([A-Za-z0-9\-]+)(\.[a-z]+)+)'

while data:
    result = re.search(pattern, data)
    if result:
        print(result[0])
    data = input()
