string = input()
new_string = ""
while string != "End":
    if string == "SoftUni":
        string = input()
        continue
    else:
        for char in string:
            new_string += 2 * char
        print(new_string)
        new_string = ""
        string = input()
