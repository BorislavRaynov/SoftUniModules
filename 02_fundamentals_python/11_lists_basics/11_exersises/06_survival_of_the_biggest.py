list_of_numbers = input().split()
count_removed_nums = int(input())
new_list = []

for element in list_of_numbers:
    new_list.append(int(element))
for num in range(count_removed_nums):
    digit = min(new_list)
    new_list.remove(digit)

print(*new_list, sep=", ")
