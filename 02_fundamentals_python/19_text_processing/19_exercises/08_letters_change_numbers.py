def check_starts_with(string):
    if ord(string[0:1:]) in range(97, 123):
        return "lower"
    return "upper"


def first_to_do(string):
    searched_number = int(string[1:-1])
    divider = ord(string[0:1:]) - 64
    multiplier = ord(string[0:1:]) - 96
    if check_starts_with(string) == "upper":
        return searched_number / divider
    else:
        return searched_number * multiplier


def check_finish_with(string):
    if ord(string[-1]) in range(97, 123):
        return "lower"
    return "upper"


def second_to_do(string):
    add_number = ord(string[-1]) - 96
    minus_number = ord(string[-1]) - 64
    if check_finish_with(string) == "upper":
        return first_to_do(string) - minus_number
    return first_to_do(string) + add_number


text = input().split()
result = 0

for word in text:
    result += second_to_do(word)

print(f"{result:.2f}")
