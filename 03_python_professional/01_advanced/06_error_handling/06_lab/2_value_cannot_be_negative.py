class ValueCannotBeNegative(Exception):
    pass


for n in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative
