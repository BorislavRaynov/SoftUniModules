import sys
test_line = input()

max_number = - sys.maxsize

while test_line != "Stop":
    test_line = int(test_line)
    if test_line > max_number:
        max_number = test_line
    test_line = input()
print(max_number)