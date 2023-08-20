num = input()
new_num = sorted(num, reverse=True)

for item in new_num:
    print(int(item), end="")
