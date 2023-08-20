text = list(input())
reversed_text = []

for i in range(len(text)):
    reversed_text.append(text.pop())

print("".join(reversed_text))
