def type_check(data):
    def decorator(func):
        def wrapper(n):
            if isinstance(n, data):
                return func(n)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

