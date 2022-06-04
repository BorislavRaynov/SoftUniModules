start_character = int(input())
stop_character = int(input())

for digit in range(start_character, stop_character + 1):
    print(chr(digit), end=" ")
