from functools import reduce


def operate(operator, *args):
    if operator == "+":
        return reduce(lambda x, y: x + y, args)
    elif operator == "-":
        return reduce(lambda x, y: x - y, args)
    elif operator == "*":
        return reduce(lambda x, y: x * y, args)
    elif operator == "/":
        if args.count(0) == 0:
            return reduce(lambda x, y: x / y, args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 8, 4))
