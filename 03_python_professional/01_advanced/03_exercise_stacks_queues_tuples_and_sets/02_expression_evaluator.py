
from functools import reduce
string = input().split()
temp_result = []
symbols = ['*', '/', '+', '-']

for element in string:
    if element not in symbols:
        temp_result.append(int(element))
    else:
        if element == "*":
            temp_result = [reduce(lambda x, y: x * y, temp_result)]
        elif element == "/":
            temp_result = [reduce(lambda x, y: x // y, temp_result)]
        elif element == "-":
            temp_result = [reduce(lambda x, y: x - y, temp_result)]
        elif element == "+":
            temp_result = [reduce(lambda x, y: x + y, temp_result)]

print(temp_result[0])
