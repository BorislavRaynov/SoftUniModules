string = input()
new_list = []

for index, value in enumerate(string):
    if value.isupper():
        new_list.append(index)
print(new_list)

# new_list = []
# for element in string:
#     if element.isupper():
#         index = string.index(element)
#         new_list.append(index)

# print(new_list)

