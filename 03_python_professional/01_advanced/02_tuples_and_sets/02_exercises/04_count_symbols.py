text = input()
sort_text = sorted(text)
info_characters = {}
for char in sort_text:
    if char not in info_characters:
        info_characters[char] = 0
    info_characters[char] += 1

for symbol, occurrence in info_characters.items():
    print(f"{symbol}: {occurrence} time/s")
