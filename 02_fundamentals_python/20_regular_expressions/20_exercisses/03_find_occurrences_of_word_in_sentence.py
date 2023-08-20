import re

data = input()
searched_word = input()
pattern = fr'\b{searched_word}\b'
result = re.findall(pattern, data, re.IGNORECASE)
print(len(result))
