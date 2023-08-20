numbers = input().split()
abs_list = []

for element in numbers:
    num = abs(float(element))
    abs_list.append(num)

print(abs_list)
