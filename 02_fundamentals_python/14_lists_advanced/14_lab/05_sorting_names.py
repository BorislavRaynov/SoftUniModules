string = input().split(", ")

sorted_lst = sorted(string, key=lambda x: (-len(x), x))

print(sorted_lst)
