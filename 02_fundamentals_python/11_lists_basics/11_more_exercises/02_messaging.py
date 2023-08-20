numbers = input(). split()
some_text = input()
split_text = []
message = []

for i in range(len(some_text)):
    split_text.append(some_text[i])

for element in numbers:
    current_sum = 0
    for i in range(len(element)):
        current_sum += int(element[i])
    if current_sum > len(split_text):
        current_sum -= len(split_text)

    message.append(split_text[current_sum])
    split_text.remove(split_text[current_sum])

print(*message, sep="")
