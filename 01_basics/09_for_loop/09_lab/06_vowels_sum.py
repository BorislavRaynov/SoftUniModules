text = input()
length = len(text)

total_sum = 0
for letter in text:
    if letter == "a":
        total_sum += 1
    elif letter == "e":
        total_sum += 2
    elif letter == "i":
        total_sum += 3
    elif letter == "o":
        total_sum += 4
    elif letter == "u":
        total_sum += 5
print(total_sum)