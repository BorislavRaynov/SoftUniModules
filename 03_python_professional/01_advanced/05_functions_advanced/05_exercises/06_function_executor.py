def func_executor(*args):
    result = ''
    for f in args:
        func_name = f[0].__name__
        current_result = f[0](*f[1])
        result += f"{func_name} - {current_result}" + '\n'
    return result


def sum_numbers(num1, num2):
    result = num1 + num2
    return result


def multiply_numbers(num1, num2):
    result = num1 * num2
    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
