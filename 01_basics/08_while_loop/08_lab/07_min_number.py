import sys
test_line = input()

min_number = sys.maxsize

while test_line != "Stop":
    test_line = int(test_line)
    if test_line < min_number:
        min_number = test_line
    test_line = input()
print(min_number)