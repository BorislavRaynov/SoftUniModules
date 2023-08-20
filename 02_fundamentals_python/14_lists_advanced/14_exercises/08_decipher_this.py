secret_message = input().split()

final_message = []

for element in secret_message:
    first_letter = ""
    rest_letters = ""
    current_word = ""
    for character in element:
        if character.isdigit():
            first_letter += character
        else:
            rest_letters += character
    if len(rest_letters) >= 2:
        current_word = chr(int(first_letter)) + rest_letters[-1] + rest_letters[1:-1] + rest_letters[0]
    else:
        current_word = chr(int(first_letter)) + rest_letters
    final_message.append(current_word)

print(" ".join(final_message))
