string = input()
current_string = ""
for index in range(len(string)):
    if index == len(string) - 2 and string[index] == string[index + 1]:
        current_string += string[index]
        break
    elif index == len(string) - 2 and string[index] != string[index + 1]:
        current_string += string[index]
        current_string += string[index + 1]
        break
    elif string[index] != string[index + 1]:
        current_string += string[index]
print(current_string)
