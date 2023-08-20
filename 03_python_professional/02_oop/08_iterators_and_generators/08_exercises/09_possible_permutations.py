from itertools import permutations


def possible_permutations(text: list):
    for el in permutations(text):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
