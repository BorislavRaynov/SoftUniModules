def sum_numbers(a, b):
    return a + b


def subtract(sum, c):
    return sum - c


def add_and_subtract(a, b, c):
    sum_of_two = sum_numbers(a, b)
    result = subtract(sum_of_two, c)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))
