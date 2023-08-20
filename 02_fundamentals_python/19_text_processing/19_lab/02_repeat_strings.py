string = input().split()
new_string = ""
for word in string:
    new_string += word * len(word)
print(new_string)
