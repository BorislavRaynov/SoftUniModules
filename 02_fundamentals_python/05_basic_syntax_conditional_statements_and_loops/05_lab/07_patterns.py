num = int(input())

for line in range(num + 1):
    print(line * "*")
for sec_line in range(num -1, -1, -1):
    print(sec_line * "*")
