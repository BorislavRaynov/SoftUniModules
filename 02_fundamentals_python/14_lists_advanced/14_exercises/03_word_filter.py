text = input().split()

new_text = [element for element in text if len(element) % 2 == 0]

print("\n".join(new_text))
