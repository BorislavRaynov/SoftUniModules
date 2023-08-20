num = int(input())

for first_character in range(num):
    for second_character in range(num):
        for third_character in range(num):
            print(f"{chr(97 + first_character)}{chr(97 + second_character)}{chr(97 + third_character)}")
                  