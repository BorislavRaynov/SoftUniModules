file_path = './numbers.txt'

file = open(file_path, 'r')
nums_sum = 0
for line in file:
    nums_sum += int(line)
print(nums_sum)
