first = input()
second = input()

new_word = first
for i in range(len(first)):
    left = second[:i + 1]
    right = first[i + 1:]
    current = left + right
    if current == new_word:
        continue
    print(current)
    new_word = current
