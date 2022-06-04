number_lines = int(input())

string_is_balanced = False
first_mark = ""
second_mark = ""
for mark in range(1, number_lines + 1):
    current_string = input()
    if mark % 2 == 0:
        current_mark = current_string
    
