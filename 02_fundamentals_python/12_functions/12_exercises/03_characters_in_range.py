def ascii_string(a, b):
    final_string = []
    first_limit = ord(a)
    second_limit = ord(b)
    for character in range(first_limit + 1, second_limit):
        letter = chr(character)
        final_string.append(letter)
    result = " ".join(final_string)
    return result


first_letter = input()
second_letter = input()
print(ascii_string(first_letter, second_letter))

