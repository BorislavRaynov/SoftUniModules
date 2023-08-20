import re
num = int(input())

for string in range(num):
    text = input()
    pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})]'
    valid_string = re.search(pattern, text)
    if valid_string:
        command, message = valid_string.groups()
        message_as_nums = []
        for character in message:
            current_num = ord(character)
            message_as_nums.append(str(current_num))
        print(f"{command}: {' '.join(message_as_nums)}")
    else:
        print("The message is invalid")
