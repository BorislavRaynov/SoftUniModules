def logged(function):
    def wrapped(*args):
        res = ''
        res += f"you called {function.__name__}{args}\n"
        res += f"it returned {function(*args)}"
        return res
    return wrapped


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
