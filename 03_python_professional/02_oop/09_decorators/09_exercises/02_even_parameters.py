def even_parameters(function):
    def wrapped(*nums):
        if all((isinstance(n, int) and n % 2 == 0) for n in nums):
            return function(*nums)
        return "Please use only even numbers!"
    return wrapped


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
