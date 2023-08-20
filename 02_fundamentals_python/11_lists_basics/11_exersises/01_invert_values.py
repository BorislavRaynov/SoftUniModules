string = input()
my_list = string.split()
my_new_list = []
for i, v in enumerate(my_list):
    my_new_list.append(-int(v))
print(my_new_list)
