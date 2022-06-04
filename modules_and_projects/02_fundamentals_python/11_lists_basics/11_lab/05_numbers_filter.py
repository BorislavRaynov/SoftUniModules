num = int(input())

full_list = []
even_list = []
odd_list = []
positive_list = []
negative_list = []

for _ in range(num):
    current_num = int(input())
    full_list.append(current_num)

command = input()

for i in range(len(full_list)):
    element = full_list[i]
    if element % 2 == 0 and command == "even":
        even_list.append(element)
    elif element % 2 != 0 and command == "odd":
        odd_list.append(element)
    elif element >= 0 and command == "positive":
        positive_list.append(element)
    elif element < 0 and command == "negative":
        negative_list.append(element)

if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "positive":
    print(positive_list)
else:
    print(negative_list)
