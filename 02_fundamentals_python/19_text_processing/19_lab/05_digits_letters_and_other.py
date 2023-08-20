def nums_in_string(current_string):
    return "".join([num for num in current_string if num.isdigit()])


def letter_in_string(current_string):
    return "".join([num for num in current_string if num.isalpha()])


def symbol_in_string(current_string):
    return "".join([num for num in current_string if not num.isalpha() and not num.isdigit()])


string = input()
print(nums_in_string(string))
print(letter_in_string(string))
print(symbol_in_string(string))
