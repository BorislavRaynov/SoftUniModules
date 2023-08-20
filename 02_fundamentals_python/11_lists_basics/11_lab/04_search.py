num = int(input())
word = input()

full_list = []
filtered_list = []

for _ in range(num):
    current_word = input()
    full_list.append(current_word)

print(full_list)

for _ in range(len(full_list)):
    element = full_list[_]
    if word in element:
        filtered_list.append(element)

print(filtered_list)
