from collections import deque

string = deque(input().split())

main_colours = ["red", "yellow", "blue"]
secondary_colours = ["orange", "purple", "green"]
found_colours = []

while string:
    if len(string) > 1:
        first_substring = string.popleft()
        last_substring = string.pop()
        current_substring = first_substring + last_substring
        second_substring = last_substring + first_substring
        if current_substring in main_colours or current_substring in secondary_colours:
            found_colours.append(current_substring)
        elif second_substring in main_colours or second_substring in secondary_colours:
            found_colours.append(second_substring)
        else:
            middle_length = len(string) // 2
            striped_first = first_substring[:-1:]
            striped_last = last_substring[:-1:]
            if striped_first:
                string.insert(middle_length, striped_first)
            if striped_last:
                string.insert(middle_length, striped_last)
    else:
        substring = string.popleft()
        if substring in main_colours or substring in secondary_colours:
            found_colours.append(substring)


for colour in found_colours:
    if colour == "orange":
        if "red" not in found_colours or "yellow" not in found_colours:
            found_colours.remove(colour)
    elif colour == "purple":
        if "red" not in found_colours or "blue" not in found_colours:
            found_colours.remove(colour)
    elif colour == "green":
        if "yellow" not in found_colours or "blue" not in found_colours:
            found_colours.remove(colour)

print(found_colours)
