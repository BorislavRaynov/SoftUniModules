#
# def new_string(text, multiplayer):
#     result = text * multiplayer
#     return result
#
#
# string = input()
# num = int(input())
# print(new_string(string, num))
string = input()
multiplayer = int(input())

new_string = lambda a, b: a * b

print(new_string(string, multiplayer))
