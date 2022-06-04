num = int(input())

for n in range(1, num + 1):
    new_n = "%02d" % (n,)
    if int(new_n[0]) + int(new_n[1]) == 5 or int(new_n[0]) + int(new_n[1]) == 7\
            or int(new_n[0]) + int(new_n[1]) == 11:
        print(f"{n} -> True")
        continue
    print(f"{n} -> False")
