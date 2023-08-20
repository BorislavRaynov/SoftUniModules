data = input()
new_string = ""
strength = 0
for index in range(len(data)):
    if strength > 0 and data[index] != ">":
        strength -= 1
    elif data[index] == ">":
        strength += int(data[index + 1])
        new_string += data[index]
    else:
        new_string += data[index]

print(new_string)
