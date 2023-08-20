def reverse_text(text: str):
    current_text = list(text)

    while current_text:
        yield current_text.pop()


for char in reverse_text("step"):
    print(char, end='')
