def length_is_valid(string):
    if 6 <= len(string) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def symbols_are_valid(string):
    if string.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def min_two_digits(string):
    count_digit = 0
    for character in string:
        if character.isdigit():
            count_digit += 1
    if count_digit >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


password = input()
validated = [length_is_valid(password), symbols_are_valid(password), min_two_digits(password)]

if all(validated):
    print("Password is valid")
