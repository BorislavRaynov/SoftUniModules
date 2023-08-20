text = input().upper()
current_string = ""
new_string = ""
repetition = ""

for i in range(len(text)):
    if not text[i].isdigit():
        current_string += text[i]
    else:
        for symbol in range(i, len(text)):
            if not text[symbol].isdigit():
                break
            repetition += text[symbol]
        repetition = int(repetition)
        new_string += current_string * repetition
        current_string = ""
        repetition = ""

print(f"Unique symbols used: {len(set(new_string))}")
print(new_string)
