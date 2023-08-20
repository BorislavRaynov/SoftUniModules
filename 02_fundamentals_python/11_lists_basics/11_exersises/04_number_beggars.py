list_of_sums = input().split(", ")
count_beggars = int(input())
new_list_of_sums = []
new_sum = []
counter_of_iteration = 0
for element in list_of_sums:
    new_list_of_sums. append(int(element))
while counter_of_iteration < count_beggars:
    sum_current_beggar = 0
    for i in range(counter_of_iteration, len(new_list_of_sums), count_beggars):
        sum_current_beggar += new_list_of_sums[i]
    counter_of_iteration += 1
    new_sum.append(sum_current_beggar)
print(new_sum)
