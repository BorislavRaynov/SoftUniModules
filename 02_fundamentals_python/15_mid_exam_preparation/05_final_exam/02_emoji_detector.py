import re

data = input()
nums_threshold = re.findall(r'\d', data)

total_threshold = 1
cool_emojis = []
count_emojis = 0

for num in nums_threshold:
    total_threshold *= int(num)

pattern = r'\:{2}([A-Z][a-z]{2,})\:{2}|\*{2}([A-Z][a-z]{2,})\*{2}'
valid_emojis = re.finditer(pattern, data)

for match in valid_emojis:
    current_emoji = match.group(0)
    current_threshold = 0
    count_emojis += 1
    if match.group(1):
        for character in match.group(1):
            current_threshold += ord(character)
        if current_threshold >= total_threshold:
            cool_emojis.append(current_emoji)
    elif match.group(2):
        for character in match.group(2):
            current_threshold += ord(character)
        if current_threshold >= total_threshold:
            cool_emojis.append(current_emoji)

print(f"Cool threshold: {total_threshold}")
print(f"{count_emojis} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)
