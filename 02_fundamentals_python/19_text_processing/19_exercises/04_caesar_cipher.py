text = input()
new_string = ""
for character in text:
    new_string += chr(ord(character) + 3)

print(new_string)
