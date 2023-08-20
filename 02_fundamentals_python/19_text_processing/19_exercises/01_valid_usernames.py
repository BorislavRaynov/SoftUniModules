def length_valid(text):
    if 3 <= len(text) <= 16:
        return True
    return False


def correct_symbols(text):
    for character in text:
        if not (character.isalnum() or character == "_" or character == "-"):
            return False
    return True


def redundant_symbols(text):
    if " " in text:
        return False
    return True


def pass_validity(text):
    if length_valid(text) and correct_symbols(text) and redundant_symbols(text):
        return True
    return False


data = input().split(", ")
for word in data:
    if pass_validity(word):
        print(word)
