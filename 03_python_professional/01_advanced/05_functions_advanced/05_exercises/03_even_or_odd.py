def even_odd(*args):
    command = args[-1]
    if command == "even":
        lst = [n for n in args[:-1] if n % 2 == 0]
    else:
        lst = [n for n in args[:-1] if n % 2 != 0]
    return lst


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
