first_set = set(list(map(int, input().split())))
second_set = set(list(map(int, input().split())))
num = int(input())

for i in range(num):
    command = input()
    if "Add First" in command:
        searched_nums = set(list(map(int, command.split()[2:])))
        first_set = first_set.union(searched_nums)
    elif "Add Second" in command:
        searched_nums = set(map(int, command.split()[2:]))
        second_set = second_set.union(searched_nums)
    elif "Remove First" in command:
        searched_nums = set(map(int, command.split()[2:]))
        first_set = set(number for number in first_set if number not in searched_nums)
    elif "Remove Second" in command:
        searched_nums = set(map(int, command.split()[2:]))
        second_set = set(number for number in second_set if number not in searched_nums)
    elif "Check Subset" in command:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

first_set = list(map(str, sorted(first_set)))
second_set = list(map(str, sorted(second_set)))
print(", ".join(first_set))
print(", ".join(second_set))
