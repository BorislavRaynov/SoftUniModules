key = int(input())
number_of_lines = int(input())
message = []
for i in range(number_of_lines):
    letter = input()
    ord_letter = ord(letter[0])
    new_letter = chr(ord_letter + key)
    message.append(new_letter)
print("".join(message))
