line = "".join(s for s in input().split())
character_dict = {}
for letter in line:
    if letter not in character_dict:
        character_dict[letter] = 0
    character_dict[letter] += 1
for key, value in character_dict.items():
    print(f"{key} -> {value}")

