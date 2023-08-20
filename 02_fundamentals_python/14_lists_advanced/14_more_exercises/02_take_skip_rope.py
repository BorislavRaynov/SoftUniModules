text = input()
number_lst = [character for character in text if character.isdigit()]
non_number_lst = [character for character in text if not character.isdigit()]

take_lst = []
skip_lst = []
for i in range(len(number_lst)):
    if i % 2 == 0:
        take_lst.append(number_lst[i])
    else:
        skip_lst.append(number_lst[i])
result = ""

for i in range(len(take_lst)):
    to_be_taken = int(take_lst[i])
    to_be_skipped = int(skip_lst[i])



# resulting_string = ""
# skipping_steps = 0
# taking_steps = 0
# start = 0

print(number_lst)
print(non_number_lst)
print(take_lst)
print(skip_lst)
print(resulting_string)
